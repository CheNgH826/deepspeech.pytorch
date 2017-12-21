#!/bin/bash
# run transcribe.py loading librispeech-pretrained model on lots of wav files

wav_path='./data/libri_dataset/wav'
transcribe_path='./data/libri_dataset/transcription'

for file in $wav_path/*
do
    filename=${file#*wav/}
    filename=${filename%\.wav}
    echo $file
    echo $filename
    echo $transcribe_path/${file#*wav/}
    python transcribe.py --model_path models/librispeech_pretrained.pth --audio_path ${file} \
            >> $transcribe_path/${filename}.txt
done
exit 0
