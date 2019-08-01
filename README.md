# inkPodcast

Hey! Welcome to INK github library! <br>
Glad you're with us :)

SET UP - **let's be on the same page**
knowledge base - https://github.com/karinlah/inkPodcast/wiki

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
### Get

#### Cross Podcasts
| Feature | Address | Parameters | Response |
| --- | --- | --- | --- |
| **Search** | `/get/search/all` |keyword | JSON of podcast episodes links and data|
| **Search** | `/get/search/podcast` | podcast name | JSON of podcast episodes links and data |

#### Per Podcast
| Feature | Address | Parameters | Response |
| --- | --- | --- | --- |
| **Get content table** | `/get/podcast/content` | podcast name & episode / link to an audio file| JSON with table content |
| **Get INKed MP3** | `/get/podcast/inked` | podcast name, episode / link to an audio file| link to episode, populated with ads|
| **Get Transcription** | `/get/podcast/trans` | podcast name, episode| Summarize transcription of the episode |
| **Get Tags** | `/get/podcast/tags` | podcast name, episode | list of tag|
| **Get Show Notes** | `/get/episode/show_notes` | podcast name, episode / link to an audio file | JSON of show notes |

### Set
| Feature | Address | Parameters | Response |
| --- | --- | --- | --- |
| **Add Tags** | `/podcast/set/tags/add` | podcast, episode, tag| result status |
