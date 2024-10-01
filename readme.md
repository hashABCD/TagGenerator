# TagSplitter 
A tool to convert comma separated words from a text file <br>to comma separated unique words in another text or csv file. 

### Requirements
Make sure you have the following installed:
- Python 3
- `pip` package manager

### Steps to Install

1. Clone the repository:
    ``` bash
    git clone https://github.com/hashABCD/TagGenerator.git
    ```
2. Navigate to the project directory:

    ```bash
    cd TagGenerator
    ```

3. Set up a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```


## Usage
In terminal run the script and pass path to source and destination as arguments.

### Convert to text file
```bash
python TextSplitter.py  [PATH_TO_SOURCE_FILE.txt], [PATH_TO_DESTINATION_FILE.txt] 
```

### Convert to csv file
```bash
python TextSplitter.py  [PATH_TO_SOURCE_FILE.txt], [PATH_TO_DESTINATION_FILE.csv] 
```