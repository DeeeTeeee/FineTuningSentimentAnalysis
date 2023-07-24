# Project 🚧 : NLP 

## Description 🆘

This repository contains the ressources, notebooks and web-app to the NLP-related live project I took. The readme will introduce you to all you need to know about this project, especially Natural Language Processing data by `ZINDI`, the fine tunning, deployment to [huggingface](https://huggingface.co/). 

## Article:
[Aticle on Medium] (https://medium.com/@davidanifowoshe/fine-tuning-roberta-for-covid-19-tweet-sentiment-classification-4063b85ff2e3)

## Assignments 📝 
I fine tunned three models from the huggingface models:
"roberta-base", "xlnet-base-cased" and "bert-base-uncased"


## Setup ⚙️ 
Install the required packages to be able to run the evaluation locally.

You need to have [`Python3`](https://www.python.org/) on your system. Then you can clone this repo and being at the repo's root (`root :: repo_name> ...`)  follow the steps below:

- Windows:
        
        python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

- Linux & MacOs:
        
        python3 -m venv venv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

The both long command-lines have a same structure, they pipe multiple commands using the symbol **;** but you may manually execute them one after another.

1. **Create the Python's virtual environment** that isolates the required libraries of the project to avoid conflicts;
2. **Activate the Python's virtual environment** so that the Python kernel & libraries will be those of the isolated environment;
3. **Upgrade Pip, the installed libraries/packages manager** to have the up-to-date version that will work correctly;
4. **Install the required libraries/packages** listed in the `requirements.txt` file so that it will be allow to import them into the python's scripts and notebooks without any issue.
## Requrements:
!pip install datasets\
!pip install sentencepiece\
!pip install transformers datasets\
!pip install transformers[torch]\
!pip install accelerate\
!pip install accelerate>=0.20.1\
!pip install huggingface_hub\
!pip3 install -q transformers datasets

🚀 **Web-App Usage**
-----------------
To see how my app works:
I have hosted it on huggingface for the public to use:
[Huggingface](https://deeeteeee01-sentimentanalysis.hf.space)


👥 **Authors**
=================

This project was developed and maintained by:
## David Anifowoshe
Feel free to reach out to me with any questions or feedback!

✨ **Acknowledgments**
=================

I would like to express my gratitude to The `Azubi Africa` team for their valuable contributions to this project.

📞 **Contact**
=================

For any questions, concerns, or suggestions regarding  this project, please contact me at [mail](david.olatomiwa@yandex.com); [mailme](dtommyanny@gmial.com).

**NB:** For MacOs users, please install `Xcode` if you have an issue.

## Ressources
1. [Quick intro to NLP](https://www.youtube.com/watch?v=CMrHM8a3hqw)
1. [Getting Started With Hugging Face in 15 Minutes](https://www.youtube.com/watch?v=QEaBAZQCtwE)
1. [Fine-tuning a Neural Network explained](https://www.youtube.com/watch?v=5T-iXNNiwIs)
1. [Fine-Tuning-DistilBert - Hugging Face Transformer for Poem Sentiment Prediction | NLP](https://www.youtube.com/watch?v=zcW2HouIIQg)
1. [Introduction to NLP: Playlist](https://www.youtube.com/playlist?list=PLM8wYQRetTxCCURc1zaoxo9pTsoov3ipY)
