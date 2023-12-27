import linkedin_json_data
import text_content_generator
import linkedin_prompts
import text_getter
import time
def main():

    file_path = "linkedin_topic.txt"  # Replace with the actual file path
    current_line = 0
    while True:
        next_line, current_line = text_getter.get_next_line_from_file(file_path, current_line)

        if next_line is not None:
            selected_text = next_line
            print(selected_text)
            print("")
            prompt =  linkedin_prompts.prompt.format(role_and_target_audience = selected_text)
            text_content = text_content_generator.openai_generate(prompt)
            print(text_content)
            print("")
            linkedin_json_data.create_text_post(text_content)
            time.sleep(21600)
        else:
            print("All Linkedin posts have been Published.")
            break
if __name__ == "__main__":
    main()