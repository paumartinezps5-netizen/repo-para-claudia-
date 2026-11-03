#!/bin/bash
# targeta -> pla general (codi + monitor + led) -> zoom al monitor -> primer pla del led -> targeta final
set -e
FFMPEG="$(cat ff.txt)"; OUT="$1"
FB=arialbd.ttf; FR=arial.ttf
W=1280; H=720; FPS=30; XF=0.5; COL=0x2E7D32
CARD=2.4; END=2.4
GS=0.5; GE=9.0      # pla general
ZS=9.0; ZE=13.5     # zoom al monitor sèrie
BS=0.0; BE=4.4      # primer pla del led (b.mp4, vertical)
p(){ python -c "print(round($1,3))"; }
G=$(p "$GE-$GS"); Z=$(p "$ZE-$ZS"); B=$(p "$BE-$BS")
O1=$(p "$CARD-$XF"); O2=$(p "$O1+$G-$XF"); O3=$(p "$O2+$Z-$XF"); O4=$(p "$O3+$B-$XF")
TOT=$(p "$O4+$END")
LOOK="hqdn3d=2:2:4:4,eq=contrast=1.07:saturation=1.12:brightness=0.01,unsharp=5:5:0.6,fps=$FPS,format=yuv420p,setsar=1"
L(){ echo "drawtext=fontfile=$FB:text='$1':fontsize=38:fontcolor=white:box=1:boxcolor=$COL@0.88:boxborderw=16:x=(w-tw)/2:y=h-110:enable='between(t,$2,$3)':alpha='min(1,min((t-$2)/0.2,($3-t)/0.2))'"; }
ENC="-c:v libx264 -preset medium -threads 2 -crf 14 -pix_fmt yuv420p -an"
"$FFMPEG" -hide_banner -loglevel error -y -threads 1 -ss $GS -to $GE -i a.mp4 -filter_threads 1 -vf "setpts=PTS-STARTPTS,scale=$W:$H:force_original_aspect_ratio=increase:flags=lanczos,crop=$W:$H,$LOOK,$(L 'Escrivim un número al monitor sèrie' 0.3 $(p "$G-0.3"))" $ENC g.mp4
"$FFMPEG" -hide_banner -loglevel error -y -threads 1 -ss $ZS -to $ZE -i a.mp4 -filter_threads 1 -vf "setpts=PTS-STARTPTS,crop=300:169:378:16,scale=$W:$H:flags=lanczos,$LOOK,$(L 'L’Arduino ens contesta pel monitor' 0.3 $(p "$Z-0.3"))" $ENC z.mp4
"$FFMPEG" -hide_banner -loglevel error -y -threads 1 -ss $BS -to $BE -i b.mp4 -filter_threads 1 -filter_complex "[0:v]setpts=PTS-STARTPTS,split[x][y];[x]scale=$W:$H:force_original_aspect_ratio=increase,crop=$W:$H,boxblur=20:2,eq=brightness=-0.08[bg];[y]scale=-2:$H:flags=lanczos[fg];[bg][fg]overlay=(W-w)/2:0,$LOOK,$(L 'El led del port 13 fa les pampallugues' 0.3 $(p "$B-0.3"))" $ENC b2.mp4
CARDV="color=c=$COL:s=${W}x${H}:r=$FPS:d=$CARD,drawbox=x=90:y=330:w=90:h=6:color=white@0.9:t=fill,\
drawtext=fontfile=$FB:text='Tasca 5':fontsize=96:fontcolor=white:x=90:y=210,\
drawtext=fontfile=$FR:text='Led i monitor sèrie':fontsize=48:fontcolor=white:x=90:y=365,\
drawtext=fontfile=$FR:text='Pau Martínez i Enric Vinyes · Robòtica · 1r Batxillerat':fontsize=28:fontcolor=white@0.8:x=90:y=620,fade=t=in:st=0:d=0.4,format=yuv420p,setsar=1"
ENDV="color=c=$COL:s=${W}x${H}:r=$FPS:d=$END,drawbox=x=90:y=330:w=90:h=6:color=white@0.9:t=fill,\
drawtext=fontfile=$FB:text='Escrivim n':fontsize=80:fontcolor=white:x=90:y=225,\
drawtext=fontfile=$FR:text='i el led fa n pampallugues':fontsize=48:fontcolor=white:x=90:y=365,format=yuv420p,setsar=1"
AUDIO="[5:a]atrim=0:$TOT,asetpts=PTS-STARTPTS,volume=0.6,afade=t=in:d=0.8,afade=t=out:st=$(p "$TOT-1.5"):d=1.5,loudnorm=I=-16:TP=-1.5[a]"
"$FFMPEG" -hide_banner -loglevel error -y -f lavfi -i "$CARDV" -i g.mp4 -i z.mp4 -i b2.mp4 -f lavfi -i "$ENDV" -i musica.m4a -filter_complex \
"[0:v]settb=1/30[k];[1:v]settb=1/30[g];[2:v]settb=1/30[z];[3:v]settb=1/30[b];[4:v]settb=1/30[e];\
[k][g]xfade=transition=fade:duration=$XF:offset=$O1[a1];[a1][z]xfade=transition=fade:duration=$XF:offset=$O2[a2];\
[a2][b]xfade=transition=fade:duration=$XF:offset=$O3[a3];[a3][e]xfade=transition=fade:duration=$XF:offset=$O4,fade=t=out:st=$(p "$TOT-0.6"):d=0.6,format=yuv420p[v];$AUDIO" \
-map "[v]" -map "[a]" -t $TOT -c:v libx264 -preset medium -threads 2 -crf 21 -profile:v main -level 3.1 -c:a aac -b:a 160k -ar 44100 -movflags +faststart "$OUT"
echo "ok $TOT"
