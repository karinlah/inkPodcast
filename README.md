# inkPodcast

Hey! Welcome to INK github library! <br>
Glad you're with us :)

SET UP - **let's be on the same page**

`git clone with SSH git@github.com:karinlah/inkPodcast.git`

- if you don't have yet a SSH key, generate a new one and add it to the ssh-agent
follow the instructions
https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

**working with git**:

- pull from master `git pull origin master`
- create you own branch `git checkout -b [name_of_your_new_branch]`
- after checking, push your branch `git push origin [name_of_your_new_branch]`

**install requirements**
`pip3 install -r requirements.txt`

**Hello World test**
* `python app.py`
* lunch to `http://localhost:5000/`

## API Endpoints

| Feature | Address | Inputs | Outputs | Privacy |
| --- | --- | --- | --- | --- |
| **Search** | `/search` | | | Public |
| **Transcription** | `/get/trans` | | | Public |
| **Set Tags** | `/set/tags` | | | Private |
| **Add Tags** | `/set/tags/add` | | | Private |
| **Get Tags** | `/get/tags` | | | Public |
| **Show Notes** | `/get/show_notes` | | | Public |
| **Get Host** | `/get/podcast/host` | | | Public |
| *Get Copyright* | `/get/podcast/copyright` | | | Public |
| *Get Name* | `/get/podcast/name` | | | Public |
| *Get Email* | `/get/podcast/email` | | | Public |
| **Get Episodes** | `/get/podcast/episodes` | | | Public |
| **Get Description** | `/get/episode/description` | | | Public |
| **Get Episode** | `/get/episode` | | | Public |
| **Get Duration** | `/get/episode/duration` | | | Public |
| **Get Publication Date** | `/get/episode/pub` | | | Public |
| **Get Image** | `/get/episode/image` | | | Public |
| **Get MP3** | `/get/episode/mp3` | | | Public |




## Database Fields

