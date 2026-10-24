#!/bin/bash
# targeta inicial -> pla general (muntatge) -> cicle retallat amb etiquetes -> targeta final
set -e
IN="$1"; OUT="$2"
FB=arialbd.ttf; FR=arial.ttf
W=720; H=1280; FPS=30; XF=0.5
CARD=2.2; END=2.0
GS=14.0; GE=17.5          # pla general
SS=2.2; TO=13.9           # el cicle, agafat del primer muntatge (net)
G=$(python -c "print(round($GE-$GS,3))"); C=$(python -c "print(round($TO-$SS,3))")
O1=$(python -c "print(round($CARD-$XF,3))"); O2=$(python -c "print(round($O1+$G-$XF,3))"); O3=$(python -c "print(round($O2+$C-$XF,3))")
TOT=$(python -c "print(round($O3+$END,3))")
TMP=tmpv; mkdir -p tmpv
"$FFMPEG" -hide_banner -loglevel error -y -threads 1 -ss $GS -to $GE -i "$IN" -filter_threads 1 -vf "vidstabdetect=shakiness=6:accuracy=15:result=$TMP/g.trf" -f null -
LOOK="hqdn3d=2:2:4:4,eq=contrast=1.07:saturation=1.15:brightness=0.015,unsharp=5:5:0.5,fps=$FPS,format=yuv420p,setsar=1"
# etiqueta amb entrada/sortida suau
L(){ echo "drawtext=fontfile=$FB:text='$1':fontsize=40:fontcolor=white:box=1:boxcolor=0xD9480F@0.85:boxborderw=18:x=(w-tw)/2:y=h-170:enable='between(t,$2,$3)':alpha='min(1,min((t-$2)/0.2,($3-t)/0.2))'"; }
EX="$(L 'Verd cotxes · vermell vianants' 0.1 5.3),$(L 'Groc' 5.3 6.8),$(L 'Vermell cotxes' 6.8 7.8),$(L 'Verd vianants' 7.8 10.8),$(L 'Verd vianants intermitent' 10.8 12.0),$(L 'Torna a començar' 12.0 12.9)"
GV="setpts=PTS-STARTPTS,vidstabtransform=input=$TMP/g.trf:smoothing=30:zoom=5,scale=$W:$H:force_original_aspect_ratio=increase:flags=lanczos,crop=$W:$H,$LOOK,$(L 'El muntatge' 0.3 $(python -c "print($G-0.3)"))"
CV="setpts=PTS-STARTPTS,vidstabtransform=input=$TMP/c.trf:smoothing=30:zoom=4,crop=340:604:0:120,scale=$W:$H:force_original_aspect_ratio=increase:flags=lanczos,crop=$W:$H,$LOOK,$EX"
CARDV="color=c=0xD9480F:s=${W}x${H}:r=$FPS:d=$CARD,drawbox=x=70:y=560:w=80:h=6:color=white@0.9:t=fill,\
drawtext=fontfile=$FB:text='Tasca 4':fontsize=86:fontcolor=white:x=70:y=440,\
drawtext=fontfile=$FR:text='Semàfor':fontsize=44:fontcolor=white:x=70:y=600,\
drawtext=fontfile=$FR:text='Pau Martínez i Enric Vinyes':fontsize=30:fontcolor=white@0.8:x=70:y=1110,\
drawtext=fontfile=$FR:text='Robòtica · 1r Batxillerat':fontsize=30:fontcolor=white@0.8:x=70:y=1155,fade=t=in:st=0:d=0.4,format=yuv420p,setsar=1"
ENDV="color=c=0xD9480F:s=${W}x${H}:r=$FPS:d=$END,drawbox=x=70:y=560:w=80:h=6:color=white@0.9:t=fill,\
drawtext=fontfile=$FB:text='Cicle de 12,7 s':fontsize=64:fontcolor=white:x=70:y=460,\
drawtext=fontfile=$FR:text='i es repeteix sol':fontsize=44:fontcolor=white:x=70:y=600,format=yuv420p,setsar=1"
AUDIO="[4:a]atrim=0:$TOT,asetpts=PTS-STARTPTS,volume=0.6,afade=t=in:d=0.8,afade=t=out:st=$(python -c "print(round($TOT-1.5,3))"):d=1.5,loudnorm=I=-16:TP=-1.5[a]"
ENC="-c:v libx264 -preset medium -threads 2 -crf 14 -pix_fmt yuv420p -an"
"$FFMPEG" -hide_banner -loglevel error -y -threads 1 -ss $GS -to $GE -i "$IN" -filter_threads 1 -vf "$GV" $ENC $TMP/g.mp4
"$FFMPEG" -hide_banner -loglevel error -y -threads 1 -ss $SS -to $TO -i tasca4_semafor.mp4 -vf "setpts=PTS-STARTPTS" $ENC $TMP/c.mp4
"$FFMPEG" -hide_banner -loglevel error -y -f lavfi -i "$CARDV" -i $TMP/g.mp4 -i $TMP/c.mp4 -f lavfi -i "$ENDV" -i musica.m4a  -filter_complex "[1:v]settb=1/30[g];[2:v]settb=1/30[c];[0:v]settb=1/30[k];[3:v]settb=1/30[e];[k][g]xfade=transition=fade:duration=$XF:offset=$O1[a1];[a1][c]xfade=transition=fade:duration=$XF:offset=$O2[a2];[a2][e]xfade=transition=fade:duration=$XF:offset=$O3,fade=t=out:st=$(python -c "print(round($TOT-0.6,3))"):d=0.6,format=yuv420p[v];$AUDIO"  -map "[v]" -map "[a]" -t $TOT -c:v libx264 -preset medium -threads 2 -crf 21 -profile:v main -level 3.1 -c:a aac -b:a 160k -ar 44100 -movflags +faststart "$OUT"
rm -rf "$TMP"
