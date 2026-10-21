#!/bin/bash
# edit2.sh entrada sortida inici final "Tasca N" "Subtítol" "drawtext extra del clip (pot ser buit)"
set -e
IN="$1"; OUT="$2"; SS="$3"; TO="$4"; T1="$5"; T2="$6"; EXTRA="$7"
D=${MUSICA_DIR:-$(dirname "$0")}
FB=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf
FR=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf
W=720; H=1280; FPS=30
CARD=2.2; XF=0.5
CLIP=$(python3 -c "print(round($TO-$SS,3))")
TOT=$(python3 -c "print(round($CARD+$CLIP-$XF,3))")
TMP=$(mktemp -d)

ffmpeg -hide_banner -loglevel error -y -ss "$SS" -to "$TO" -i "$IN" \
  -vf "vidstabdetect=shakiness=6:accuracy=15:result=$TMP/t.trf" -f null -

CLIPV="setpts=PTS-STARTPTS,vidstabtransform=input=$TMP/t.trf:smoothing=15:zoom=4,scale=$W:$H:force_original_aspect_ratio=increase:flags=lanczos,crop=$W:$H,\
hqdn3d=2:2:4:4,eq=contrast=1.07:saturation=1.15:brightness=0.015,unsharp=5:5:0.5,fps=$FPS,format=yuv420p,setsar=1"
if [ -n "$EXTRA" ]; then CLIPV="$CLIPV,$EXTRA"; fi

CARDV="color=c=0x6A3D9A:s=${W}x${H}:r=$FPS:d=$CARD,\
drawbox=x=70:y=560:w=80:h=6:color=white@0.9:t=fill,\
drawtext=fontfile=$FB:text='$T1':fontsize=86:fontcolor=white:x=70:y=440,\
drawtext=fontfile=$FR:text='$T2':fontsize=44:fontcolor=white:x=70:y=600,\
drawtext=fontfile=$FR:text='Pau Martínez i Enric Vinyes':fontsize=30:fontcolor=white@0.8:x=70:y=1110,\
drawtext=fontfile=$FR:text='Robòtica · 1r Batxillerat':fontsize=30:fontcolor=white@0.8:x=70:y=1155,\
fade=t=in:st=0:d=0.4,format=yuv420p,setsar=1"

AUDIO="[1:a]highpass=f=150,lowpass=f=6000,afftdn=nf=-25:nr=25:tn=1,volume=0.25,adelay=$(python3 -c "print(int(($CARD-$XF)*1000))"):all=1,apad[orig];\
[2:a]atrim=0:$TOT,asetpts=PTS-STARTPTS,volume=0.6[mus];\
[orig][mus]amix=inputs=2:normalize=0:duration=longest,atrim=0:$TOT,afade=t=in:d=0.8,afade=t=out:st=$(python3 -c "print(round($TOT-1.5,3))"):d=1.5,loudnorm=I=-16:TP=-1.5[a]"

ffmpeg -hide_banner -loglevel error -y -f lavfi -i "$CARDV" -ss "$SS" -to "$TO" -i "$IN" -i "$D/musica.m4a" \
  -filter_complex "[1:v]$CLIPV[c];[0:v][c]xfade=transition=fade:duration=$XF:offset=$(python3 -c "print(round($CARD-$XF,3))"),fade=t=out:st=$(python3 -c "print(round($TOT-0.8,3))"):d=0.8,format=yuv420p[v];$AUDIO" \
  -map "[v]" -map "[a]" -t "$TOT" -c:v libx264 -preset slow -crf 22 -profile:v high -c:a aac -b:a 160k -ar 44100 -movflags +faststart "$OUT"
rm -rf "$TMP"
ffprobe -v error -show_entries format=duration,size -of compact "$OUT"
