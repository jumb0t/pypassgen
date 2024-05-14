import argparse
import logging
from mnemonic import Mnemonic
import colorama
from colorama import Fore, Style

def generate_mnemonic_phrases(num_phrases, words_per_phrase):
    mnemo = Mnemonic("english")  # Specify the language for the word list
    
    phrases = []
    try:
        for _ in range(num_phrases):
            # Generate a new mnemonic phrase
            phrase = mnemo.generate(strength=256)  # Use default strength (256 bits)
            
            # Split the generated phrase into a list of words
            words = phrase.split()
            
            # If the number of words per phrase is less than specified, raise an error
            if len(words) < words_per_phrase:
                raise ValueError(f"Generated phrase has only {len(words)} words, less than required {words_per_phrase} words.")
            
            # Take the first 'words_per_phrase' words to form the desired number of words per phrase
            final_phrase = " ".join(words[:words_per_phrase])
            
            phrases.append(final_phrase)
    except Exception as e:
        logging.error(f"Error occurred during mnemonic phrase generation: {e}")
        raise  # Re-raise the exception for higher-level handling

    return phrases

def write_phrases_to_file(phrases, output_file):
    try:
        with open(output_file, "w") as file:
            for phrase in phrases:
                file.write(phrase + "\n")
    except Exception as e:
        logging.error(f"Error occurred while writing phrases to file: {e}")
        raise  # Re-raise the exception for higher-level handling

def main():
    parser = argparse.ArgumentParser(
        description=f"{Fore.CYAN}Generate BIP 39 compatible mnemonic phrases and save to a file.{Style.RESET_ALL}",
        usage=f"{Fore.GREEN}%(prog)s [-p N] [-w {{12,15,18,21,24}}] [-o FILE]{Style.RESET_ALL}"
    )
    parser.add_argument(
        "-p", "--phrases", type=int, default=1,
        help=f"{Fore.YELLOW}Number of mnemonic phrases to generate (default: 1){Style.RESET_ALL}"
    )
    parser.add_argument(
        "-w", "--words", type=int, default=12, choices=[12, 15, 18, 21, 24],
        help=f"{Fore.YELLOW}Number of words per phrase (choices: 12, 15, 18, 21, 24; default: 12){Style.RESET_ALL}"
    )
    parser.add_argument(
        "-o", "--output", type=str, default=None,
        help=f"{Fore.YELLOW}Output file to save generated phrases{Style.RESET_ALL}"
    )
    
    args = parser.parse_args()
    
    num_phrases = args.phrases
    words_per_phrase = args.words
    output_file = args.output
    
    # Initialize colorama for cross-platform ANSI color support
    colorama.init()
    
    # Configure logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    
    try:
        mnemonic_phrases = generate_mnemonic_phrases(num_phrases, words_per_phrase)
        
        if output_file:
            # Write generated mnemonic phrases to the specified output file
            write_phrases_to_file(mnemonic_phrases, output_file)
            logging.info(f"{Fore.GREEN}Generated {num_phrases} mnemonic phrases with {words_per_phrase} words per phrase.{Style.RESET_ALL}")
            logging.info(f"{Fore.GREEN}Saved to: {output_file}{Style.RESET_ALL}")
        else:
            # Print generated mnemonic phrases to the console with custom coloring
            for idx, phrase in enumerate(mnemonic_phrases):
                words = phrase.split()
                first_word = words[0]
                rest_of_phrase = " ".join(words[1:])
                
                # Determine colors for the first word and the rest of the phrase
                first_word_color = Fore.GREEN
                rest_color = Fore.MAGENTA if idx % 2 == 0 else Fore.CYAN
                
                # Print the first word in green and the rest of the phrase in alternating colors
                print(f"{first_word_color}{first_word}{Style.RESET_ALL} {rest_color}{rest_of_phrase}{Style.RESET_ALL}")
    except Exception as e:
        logging.exception(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        # Display help if no arguments are provided
        print(f"{Fore.YELLOW}Usage: python mnemonic_generator.py [-p N] [-w {{12,15,18,21,24}}] [-o FILE]{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Try 'python mnemonic_generator.py --help' for more options.{Style.RESET_ALL}")
        sys.exit(1)
    
    main()

