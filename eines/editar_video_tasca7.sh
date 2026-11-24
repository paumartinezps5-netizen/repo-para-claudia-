#!/bin/bash
# targeta -> pla sencer (mà de l'Enric visible) + zoom als leds + rètols -> targeta final
# àudio: només el brunzidor (filtre de banda ~2,3 kHz + porta de soroll) + música ambient
set -e
FFMPEG="$1"; OUT="$2"   # s'executa a la carpeta amb v.mp4, amb.wav, arial*.ttf
FB=arialbd.ttf; FR=arial.ttf
W=1280; H=720; FPS=30; XF=0.5; COL=0x6A3D9A
CARD=2.6; END=2.6; V=14.0
p(){ python -c "print(round($1,3))"; }
O1=$(p "$CARD-$XF"); O2=$(p "$O1+$V-$XF"); TOT=$(p "$O2+$END")
L(){ echo "drawtext=fontfile=$FB:text='$1':fontsize=34:fontcolor=white:box=1:boxcolor=$COL@0.9:boxborderw=14:x=40:y=h-84:enable='between(t,$2,$3)':alpha='min(1,min((t-$2)/0.2,($3-t)/0.2))'"; }
LOOK="hqdn3d=2:2:4:4,eq=contrast=1.08:saturation=1.15,unsharp=5:5:0.6"
"$FFMPEG" -hide_banner -loglevel error -y -t $V -i v.mp4 -filter_complex "\
[0:v]fps=$FPS,split[a][b];\
[a]scale=-2:$H:flags=lanczos,crop=$W:$H,$LOOK[bg];\
[b]crop=288:162:521:120,scale=476:268:flags=lanczos,$LOOK,pad=484:276:4:4:white[z];\
[bg][z]overlay=x=W-w-28:y=H-h-28:enable='gte(t,1)',\
drawtext=fontfile=$FB:text='Zoom als leds':fontsize=22:fontcolor=white:box=1:boxcolor=black@0.55:boxborderw=6:x=w-484-28+10:y=h-276-28+10:enable='gte(t,1)',\
drawbox=x=0:y=80:w=420:h=330:color=$COL:t=6:enable='between(t,0,1.4)',\
$(L 'L’Enric aguanta el polsador' 0.1 1.4),$(L 'Els cotxes passen a groc i després a vermell' 1.5 3.9),\
$(L 'Verd per als vianants i 3 pitets' 4.0 6.4),$(L 'El verd parpelleja i pita cada cop més ràpid' 6.5 11.9),\
$(L 'Pitet llarg i els vianants tornen a vermell' 12.0 13.9),format=yuv420p,setsar=1[v]" \
-map "[v]" -c:v libx264 -preset medium -crf 15 -an m.mp4
CARDV="color=c=$COL:s=${W}x${H}:r=$FPS:d=$CARD,drawbox=x=90:y=330:w=90:h=6:color=white@0.9:t=fill,\
drawtext=fontfile=$FB:text='Tasca 7':fontsize=96:fontcolor=white:x=90:y=210,\
drawtext=fontfile=$FR:text='Semàfor amb polsador i brunzidor':fontsize=48:fontcolor=white:x=90:y=365,\
drawtext=fontfile=$FR:text='Pau Martínez i Enric Vinyes · Robòtica · 1r Batxillerat':fontsize=28:fontcolor=white@0.8:x=90:y=620,fade=t=in:st=0:d=0.4,format=yuv420p,setsar=1"
ENDV="color=c=$COL:s=${W}x${H}:r=$FPS:d=$END,drawbox=x=90:y=330:w=90:h=6:color=white@0.9:t=fill,\
drawtext=fontfile=$FB:text='Premem el polsador':fontsize=72:fontcolor=white:x=90:y=230,\
drawtext=fontfile=$FR:text='i els vianants poden creuar':fontsize=48:fontcolor=white:x=90:y=365,format=yuv420p,setsar=1"
BUZZ="highpass=f=1700,highpass=f=1700,lowpass=f=3200,lowpass=f=3200,afftdn=nf=-35:nr=20,agate=threshold=0.02:ratio=8:attack=2:release=60,volume=5"
"$FFMPEG" -hide_banner -loglevel error -y -f lavfi -i "$CARDV" -i m.mp4 -f lavfi -i "$ENDV" -i v.mp4 -i amb.wav -filter_complex \
"[0:v]settb=1/30[k];[1:v]settb=1/30[m];[2:v]settb=1/30[e];\
[k][m]xfade=transition=fade:duration=$XF:offset=$O1[a1];[a1][e]xfade=transition=fade:duration=$XF:offset=$O2,fade=t=out:st=$(p "$TOT-0.6"):d=0.6,format=yuv420p[v];\
[3:a]atrim=0:$V,asetpts=PTS-STARTPTS,aformat=channel_layouts=mono,$BUZZ,adelay=$(p "$O1*1000"):all=1,apad[bz];\
[4:a]atrim=0:$TOT,asetpts=PTS-STARTPTS,volume='if(between(t,$CARD,$O2+0.3),0.22,0.55)':eval=frame,afade=t=in:d=0.8,afade=t=out:st=$(p "$TOT-1.5"):d=1.5[mu];\
[bz][mu]amix=inputs=2:duration=longest:normalize=0,atrim=0:$TOT,loudnorm=I=-16:TP=-1.5,aformat=channel_layouts=stereo[a]" \
-map "[v]" -map "[a]" -t $TOT -c:v libx264 -preset medium -crf 21 -profile:v main -level 3.1 -c:a aac -b:a 160k -ar 44100 -movflags +faststart "$OUT"
echo "ok $TOT"
