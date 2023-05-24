![CSS](https://img.shields.io/badge/CSS-239120?&style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![Google](https://img.shields.io/badge/google-4285F4?style=for-the-badge&logo=google&logoColor=white)

# Documentation of the Flask Translate application

# introduce :
The Flask Translate app allows a user to enter text in one language and translate that text into another language. The application uses the Google Translate API to perform real-time translations.

# functionality:
1. Language selection: users can use the drop-down menu to select the source and target language.
2. Automatic translation: when the user does not know the source language of the text to be translated, the auto detection function can be used to identify the language and translate accordingly.
3. Results display: once the user has submitted the form, the translated text is displayed in a dedicated text field on the right side of the page.

# HTML code:
The HTML code of the user interface consists of several key elements:
- A form with a source text field, source and target language drop-down menus, and a submit button.
- A container to display the translation results, represented by a read-only text field.

# JavaScript code:
The JavaScript code included in the page performs the following:
- Attach an event handler to the submission form to call the translation function.
- The translation function retrieves the source text, the source language and the target language selected by the user.
- Using the Google Translate API, send a GET request to get the source text translated.
- Process the JSON response to extract the translations and display them in the result text field.

# CSS Styles:
The CSS code included in the page is used to apply styles and make the user interface more beautiful. The main styles include the formatting of forms, text fields and buttons, as well as the overall layout of the page.

# Use:
To use the application, users should follow the steps below:
1. Enter the text to be translated in the "Text to be translated" text field.
2. Select the source language from the Source Language drop-down menu.
3. Select the target language from the "Target Language" drop-down menu.
4. Click on the "Translate" button.
5. The translation of the source text will be displayed in the result text field.

Note:
The application uses the Google Translate API, so an active internet connection is required for the translation to work.

In conclusion :
Flask translation app provides users with a user-friendly interface to translate text from one language to another. It is based on the Google Translate API and uses HTML, JavaScript and CSS to create a simple and beautiful user experience.

# Install the necessary and Running the Project:

To use and run this project, you simply need to download all the files from the repository. Once the download is complete, extract the files and follow these steps:

1. Install the required packages/libraries by running the following commands in your terminal:

Install the `requests` library:
   
      pip install requests

Install the `langdetect` library:

      pip install langdetect

Install the `flask` library:

      pip install flask

2. After installing the packages, run the Python file.

3. In the terminal, an IP address should appear. You can either click on it directly or copy/paste the IP address into a browser to access the online translator.

Once all the step above completed you can write and translate a word or sentance in the langages available to you. If you don't know the origin langage you can use the auto-detect function. 
