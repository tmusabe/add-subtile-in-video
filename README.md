# Add Subtile In Video
This repository is for generating video with in built subtitle. It requires an audio transcript file with like `audio.tsv` which content text along with timestamp and a video file like `samplevideo.mp4`.

## 📋 Getting Audio Transcrible File
`audio.tsv` is the transcribe of `samplevideo.mp4` from [VALLE-X](https://github.com/Plachtaa/VALL-E-X) model.

## 💉 Installing Dependent Libraries 
```
pip install moviepy pandas
```

## 🧠 Todos
- [ ] Create a pipeline to create subtile from the video using VALLE-X
- [ ] Develop a web interface
- [ ] Support multiple language using Google Translator
- [ ] To be added...

## 📜 License
This repository is licensed under the [MIT License](./LICENSE).
