# CVScan.ai 🤖

**AI-Powered CV Review and Feedback Tool**

CVScan.ai is an intelligent application that uses Google's Gemini AI to provide instant, professional feedback on your CV/resume. Upload your document and receive personalized suggestions for improvement across multiple focus areas.

## ✨ Features

- **Multi-format Support**: Upload CVs in PDF, DOCX, or TXT formats
- **AI-Powered Analysis**: Leverages Google Gemini 2.0 Flash for intelligent feedback
- **Customizable Feedback**: Choose your preferred tone and focus areas
- **Instant Results**: Get comprehensive feedback in seconds
- **User-Friendly Interface**: Clean, intuitive Streamlit web interface

## 🎯 Focus Areas

The AI can analyze your CV across multiple dimensions:

- **Grammar & Language**: Spelling, punctuation, and language clarity
- **Formatting**: Layout, structure, and visual presentation
- **Keyword Optimization**: ATS-friendly content and industry-specific terms
- **Overall Impact**: Professional impression and effectiveness

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd CVScan.ai
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run main.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:8501`

## 📋 Requirements

The project uses the following key dependencies:

- `streamlit` - Web application framework
- `google-generativeai` - Google Gemini AI integration
- `PyPDF2` - PDF text extraction
- `python-docx2txt` - DOCX text extraction
- `python-dotenv` - Environment variable management

## 🔧 Usage

1. **Upload Your CV**: Click the file uploader and select your CV file (PDF, DOCX, or TXT)
2. **Choose Tone**: Select your preferred feedback tone (Professional, Friendly, or Direct)
3. **Select Focus Areas**: Choose which aspects of your CV to analyze
4. **Get Feedback**: Click "Review my CV" and wait for AI-generated feedback
5. **Review Results**: Read through the numbered feedback points and suggestions

## 🛠️ Technical Details

### Architecture

- **Frontend**: Streamlit web interface
- **Backend**: Python with Google Gemini AI integration
- **File Processing**: Multi-format text extraction
- **AI Model**: Gemini 2.0 Flash for natural language processing

### Key Functions

- `extract_text()`: Handles multiple file formats and extracts text content
- `build_prompt()`: Constructs AI prompts based on user preferences
- `review_cv()`: Interfaces with Gemini AI for feedback generation
- `main()`: Streamlit application entry point

## 🔑 API Configuration

To use this application, you'll need a Google Gemini API key:

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Add it to your `.env` file as `GEMINI_API_KEY`

## 📁 Project Structure

```
CVScan.ai/
├── main.py          # Main application file
├── pyproject.toml   # Project configuration
├── requirements.txt  # Python dependencies
├── .env            # Environment variables (create this)
└── README.md       # This file
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/CVScan.ai/issues) page
2. Create a new issue with detailed information
3. Include your Python version and any error messages

## 🔮 Future Enhancements

- [ ] Support for more file formats (RTF, ODT)
- [ ] Multiple language support
- [ ] CV template suggestions
- [ ] Export feedback to PDF
- [ ] Integration with job application platforms
- [ ] ATS compatibility scoring

---

**Made with ❤️ using Streamlit and Google Gemini AI**
