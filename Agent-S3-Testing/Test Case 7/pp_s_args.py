import argparse
import subprocess

prompt_all = "Follow the instruction below carefully. Analyze the screenshot thoroughly and move the mouse to the exact position when needed. Do not interact with anything unrelated to the task. Do not switch to another applications when doing this task. Step 1. Open Microsoft Edge. If Edge is not maximized, use Win + Up else continue the task. Edge is maximized if Edge window fill the whole screen, but the title bar and taskbar remain visible (not the F11 fullscreen mode). Step 2. Go to the website https://docs.google.com. When the page is fully loaded, on the main Docs screen, look for the section labeled “Start a new document”, under that text, locate the large white rectangle with a multicolor plus icon (blue, red, yellow, green) in the center. Click inside that white rectangle (the “Blank document” option). Name this new document “Summarize.” Step 3. Open a new tab in the same Edge window. Go to {url} to access the paper. Carefully examine the paper’s format. If the paper is organized into two columns, you should read the text from the left column first, then proceed to the right column, following a top-to-bottom order. The end of a page corresponds to the bottom of the right column, while the beginning of a page corresponds to the top of the left column. Step 4. Start reading the paper section by section. Begin reading all content under this section, including any subsections. Each page only displays a portion of its content at first. Press the Space key exactly once to reveal the remaining part of the same page. A single Space press will display the full rest of that page, meaning the entire page is now completely visible. Once the rest of the page appears, continue reading until you reach the bottom of the fully revealed page, then proceed to the next step. Do not scroll down. Do not switch back to Google Docs tab to summarize before doing below steps. Step 5. When you reach the end of the current page, you must go to the next page to check whether the same section continues. How to change page: Use right arrow key to go to the next page. Do not use other toolbar buttons or scroll manually. If you can't change the page yet, keep trying until it works, do not hallucinate the image or content of the next page. Step 6. Keep reading the content until you reach the exact point where a new section title begins (for example, “5. Conclusion”, “V. Results”, etc., not Fig. or Table.). When you encounter a new section title, you must read all text above that title on the same page as part of the current section (do not conclude that the section ended on the previous page just because the new section title appears on the next page), then process to step 7. You must always check the beginning of the next page to confirm whether the current section continues. If you fully read the current page and don't see any new section title on this page, repeat step 5. Step 7. Only after fully reading the section may you stop reading and proceed to summarize the previous section. Switch to the Google Docs tab (which is a tab in the same browser, not the application, use Ctr + Tab to switch between tabs). Write a summary of the key points from what you just read for each subsections of that section. Use Ctrl + End to move to the end of the document before typing the summary, don't click anywhere. Just type the text to the document, no need to check for truncated or missing text after typing. Important summary rules: Summarize faithfully using only information present in the paper. Do not paraphrase excessively or reword in a way that changes meaning. Do not add personal opinions, comments, or inferred details beyond what the paper states. Step 8. After finishing your notes for that section, return to the paper tab using the same Edge window. Continue reading the next section. Repeat the process from step 4 to 7 until you have read and summarized all sections of the paper. Step 9. Once you have finished reading the entire paper (to the last page of it) and taking notes: Go back to the Google Docs tab. Review all your notes carefully. Combine and refine them into a complete structured summary following this format: What is the research/project about? What is its methodology? What are the results?. Step 10. After completing the full summary, download the document file from Google Docs."
prompt_1_sec = "1 section"
prompt_n_sec = "n sections"

def build_prompt(url: str, section: list[str]) -> str:
    if not section:
        return prompt_all.format(url=url)
    elif len(section) == 1:
        sec = section[0].capitalize()
        return prompt_1_sec.format(url=url, sec=sec)
    else:
        sec_list = ', '.join([s.capitalize() for s in section])
        return prompt_n_sec.format(url=url, sec_list=sec_list)

def main():
    parser = argparse.ArgumentParser(
        description="Automatic paper summarization via cli_app.py"
    )

    parser.add_argument(
        "--url", "-u",
        required=True,
        help="Link to the paper (e.g., https://arxiv.org/pdf/xxxx.xxxxx)"
    )
    parser.add_argument(
        "--section", "-p",
        nargs="*",             # can summarize many sections
        default=[],            # default: full paper
        help="Sections to summarize (e.g., introduction, methods, results)"
    )

    args = parser.parse_args()

    prompt = build_prompt(args.url, args.section)
    print(f"[INFO] Generated prompt:\n{prompt}\n")

    subprocess.run(
        ["python", "cli_app.py"],
        input=prompt,
        text=True,
        shell=True
    )

if __name__ == "__main__":
    main()