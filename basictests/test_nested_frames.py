
from playwright.sync_api import Page, expect

def test_autosuggestion(page: Page):
    page.goto("https://the-internet.herokuapp.com/nested_frames")
    main_frame = page.main_frame
    for child_frame in main_frame.child_frames:
       print(child_frame.name)
    
    top_frame = main_frame.child_frames[0]
    bottom_frame = main_frame.child_frames[1]

    left_frame = top_frame.child_frames[0]
    middle_frame = top_frame.child_frames[1]    
    right_frame = top_frame.child_frames[2]

    expect(left_frame.locator("body")).to_have_text("LEFT")
    expect(middle_frame.locator("body")).to_have_text("MIDDLE")
    expect(right_frame.locator("body")).to_have_text("RIGHT")
    expect(bottom_frame.locator("body")).to_have_text("BOTTOM")