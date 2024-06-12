import pandas as pd
from googletrans import Translator

# Initialize the translator
translator = Translator()

def translate_text(text):
    if pd.isna(text):
        return text
    try:
        # Translate the text from English to Chinese
        translation = translator.translate(text, src='en', dest='zh-cn')
        return translation.text
    except Exception as e:
        return text

# Load the Excel file
file_path = './youreg.xlsx'  # Update this to your file path
df = pd.read_excel(file_path)

# Apply the translation function to each cell in the dataframe
df_translated = df.applymap(translate_text)

# Save the translated dataframe to a new Excel file
output_path = 'yourscn.xlsx'  # Update this to your desired output file path
df_translated.to_excel(output_path, index=False)

print(f'Translated file saved to {output_path}')
