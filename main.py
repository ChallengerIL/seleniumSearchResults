from selenium import webdriver
from selenium.webdriver.common.by import By
import itertools
import time

SEQUENCE_LENGTH = 3

HEBREW_ALPHABET = ['א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט', 'י', 'כ', 'ל', 'מ', 'נ', 'ס', 'ע', 'פ', 'צ', 'ק', 'ר', 'ש', 'ת']

combinations = filter(lambda x: all(a != b for a, b in zip(x, x[1:])), itertools.product(HEBREW_ALPHABET, repeat=SEQUENCE_LENGTH))

letter_sequences = [''.join(combination) for combination in combinations]

url = 'to be changed'
search_field_locator = (By.ID, 'to be changed')
results_locator = (By.CLASS_NAME, 'to be changed')

output_file = 'results.txt'

driver = webdriver.Chrome()

try:
    driver.get(url)

    with open(output_file, 'a') as f:
        for letter_sequence in letter_sequences:
            search_field = driver.find_element(*search_field_locator)

            search_field.clear()

            search_field.send_keys(letter_sequence)

            time.sleep(.1)

            results = driver.find_elements(*results_locator)

            non_empty_results = [result.text for result in results if result.text.strip()]

            if non_empty_results:
                for result in non_empty_results:
                    f.write(result + '\n')

finally:
    driver.quit()
