#!/usr/bin/env python3
"""
Take screenshots of the TV Network application for README documentation
"""

from playwright.sync_api import sync_playwright
import os
import time

def take_screenshots():
    """Take screenshots of all main pages in the TV Network application"""

    # Create screenshots directory if it doesn't exist
    screenshots_dir = "screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)

    base_url = "https://tv-network-47u7vgy93-dennesssys-projects.vercel.app"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Set viewport to desktop size
        page.set_viewport_size({"width": 1200, "height": 800})

        # Take screenshot of main page
        print("Taking screenshot of main page...")
        page.goto(base_url)
        page.wait_for_load_state('networkidle')
        time.sleep(2)  # Wait for any animations
        page.screenshot(path=f"{screenshots_dir}/main-page.png", full_page=True)

        # Take screenshot of content management page
        print("Taking screenshot of content management page...")
        page.goto(f"{base_url}/content-management.html")
        page.wait_for_load_state('networkidle')
        time.sleep(2)
        page.screenshot(path=f"{screenshots_dir}/content-management.png", full_page=True)

        # Take screenshot of analytics page
        print("Taking screenshot of analytics page...")
        page.goto(f"{base_url}/analytics.html")
        page.wait_for_load_state('networkidle')
        time.sleep(2)
        page.screenshot(path=f"{screenshots_dir}/analytics.png", full_page=True)

        # Take screenshot of settings page
        print("Taking screenshot of settings page...")
        page.goto(f"{base_url}/settings.html")
        page.wait_for_load_state('networkidle')
        time.sleep(2)
        page.screenshot(path=f"{screenshots_dir}/settings.png", full_page=True)

        browser.close()

        print(f"Screenshots saved to {screenshots_dir}/ directory")

if __name__ == "__main__":
    take_screenshots()