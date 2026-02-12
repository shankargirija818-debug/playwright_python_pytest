from operator import index
from playwright.sync_api import Page, expect

def test_handle_dynamic_table(page: Page):
    page.goto("https://vinothqaacademy.com/webtable/")
    # Locate the table and its rows
    table_rows = page.locator("table#myTable tr")
    third_row= table_rows.nth(3)  # Indexing starts at 0, so nth(2) gives the third row
    #Extract the text from the third row
    third_row_text = third_row.text_content()
    print("Text in the third row:", third_row_text)
    checkbox = third_row.locator("td").locator("input[type='checkbox']")
    checkbox.check(timeout=50000)
    expect(checkbox).to_be_checked()

    # Extract the name and email from the third row
    name = third_row.locator("td").nth(1).text_content()  # Assuming the name is in the second column (index 1)
    email = third_row.locator("td").nth(3).text_content()  # Assuming the email is in the fourth column (index 3)
    print(f"Name: {name}, Email: {email}")

    # #extract all the datas from the table
    # index = 0
    # while index < table_rows.count():
    #     row_text = table_rows.nth(index).text_content()
    #     print(f"Row {index + 1}: {row_text}")
    #     index += 1
    # #all_rows_text = table_rows.all_text_contents()
    # #print("All rows in the table:", all_rows_text)



