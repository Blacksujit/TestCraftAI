# 🧪 MultiModel LLM Tool:

## Automated Test Instruction Generator

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python) ![Flask](https://img.shields.io/badge/Flask-2.3.2-green?style=flat-square&logo=flask) ![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Transformers-orange?style=flat-square&logo=hugging-face)

Generate automated test instructions for your software or application features using images and optional context with the power of Hugging Face's ViLT model!

## 📋 Project Overview

This project provides a web-based interface to generate test instructions using Visual Question Answering (VQA). Upload screenshots or images, provide an optional context, and let the model do the rest!

## 🚀 Features

- **Visual Question Answering:** Automatically generate test instructions based on uploaded images.
- **Context-Aware:** Include optional text context to refine the instructions.
- **Dynamic Interface:** Simple and user-friendly web interface for easy interaction.
- **Scalable:** Easily extendable with more models or features.

## 🏗️ Project Structure

``` 

├── app/
│   ├── app.py                  # Main Flask application
│   ├── uploads/                # Directory for uploaded images
│   └── utils/
│       └── llm.py              # LLM utilities (model inference functions)
├── templates/
│   └── index.html              # HTML template for the web form
├── static/
│   └── css/
│       └── styles.css          # Custom CSS for styling
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies
└── .gitignore                  # Files and directories to ignore in Git

```

## ⚙️ Setup Instructions:

### Prerequisites:

1.) Python 3.7+: Ensure you have Python installed.

2.) Pip: Make sure pip is installed to manage dependencies.

## Installation:

1. Clone the Repository:

```git clone https://github.com/Blacksujit/MultiModel_LLM_Tool

  cd multimodel-llm-tool
```

2. Create a Virtual Environment:

```
python -m venv venv

``On Windows: venv\Scripts\activate``

```

3. Install Dependencies:

```
pip install -r requirements.txt
 
```

4. Download the Model:

```
transformers-cli download dandelin/vilt-b32-finetuned-vqa

```

5. Run the Application:


```
python run.py
```

6. Access the Application:

Open your web browser and go to: http://127.0.0.1:5000


## 🖥️ Usage:

1.) Upload Images: Click on the upload button and select the images/screenshots you want to use for generating test instructions.

2.) Add Context: (Optional) Provide context to make the instructions more specific.

3.) Generate Instructions: Click the "Generate" button to receive your test instructions.
 
## 🛠️ Development:

Feel free to contribute by forking the repository, making changes, and submitting a pull request!

## To Do:
 
1.) Add support for multiple languages.

2.) Integrate more advanced models.

3.) Improve UI/UX for better interaction.

## 📝 Contributing:

Contributions are welcome! Please read the CONTRIBUTING.md for more details.

## 📜 License:

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements:

1.) **Hugging Face for the ViLT model**.

2.) **Flask for providing the web framework.**

3.) **Community contributors for their continuous support.**


### Empowering test automation with AI 🌟


