# Import Required Libraries
from gtts import gTTS  # Google Text-to-Speech library
import PyPDF2  # PDF file reader library

# Function to Extract Text from a PDF File
def get_text_from_pdf(file_path):
    try:
        # Open the PDF file in read-binary mode
        with open(file_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            extracted_text = []

            # Iterate through each page and extract text
            for page_number in range(pdf_reader.numPages):
                try:
                    page = pdf_reader.getPage(page_number)
                    extracted_text.append(page.extractText())
                except Exception as error:
                    print(f"Unable to extract text from page {page_number + 1}: {error}")

        # Combine extracted text into a single string
        return " ".join(extracted_text)
    except FileNotFoundError:
        print("Error: The specified PDF file could not be found.")
        return ""
    except Exception as error:
        print(f"An unexpected error occurred: {error}")
        return ""

# Main Program Execution
if __name__ == "__main__":
    # Prompt the user to enter the PDF file path
    input_pdf_path = input("Please enter the full path to the PDF file: ")

    # Extract text content from the specified PDF
    pdf_content = get_text_from_pdf(input_pdf_path)

    if pdf_content.strip():  # Proceed only if text is successfully extracted
        print("PDF text extraction successful!")
        print(f"Preview of extracted text:\n{pdf_content[:500]}...")  # Display first 500 characters as a preview

        # Convert the extracted text into speech
        try:
            # Set language for text-to-speech conversion
            language_code = 'en'

            # Generate the speech audio
            tts_audio = gTTS(text=pdf_content, lang=language_code, slow=False)

            # Prompt the user for the desired output MP3 filename
            output_audio_filename = input("Enter the desired name for the output audio file (e.g., 'output.mp3'): ")

            # Save the audio file
            tts_audio.save(output_audio_filename)
            print(f"Audio file successfully saved as '{output_audio_filename}'.")
        except Exception as error:
            print(f"An error occurred while generating the audio file: {error}")
    else:
        print("No text could be extracted from the PDF. Please check the file and try again.")
