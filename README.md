## HRSupervisor ##
Simple AI-based app to automatically review code in GitHub repo.

### How to launch ###
1. Install and launch Docker client on your machine
2. Create .env file and fill variables from .env.sample there
3. Execute `docker-compose up --build` in the terminal
4. Go to `localhost:8000/docs`
5. Use 'review' endpoint for GitHub repo review

### Possible improvements ###
#### What happens if there are too many requests at a time? ####
Speaking of API limits, there are 2 factors to consider:
1. In case of OpenAI rate limits, it makes sense to create a retry system in AI service
2. In case of GitHub API limits, it would be great to have a pool of keys to substitute them when the limits are reached

Speaking of system productivity, it would be great to use multi-threading.

#### What happens if there are too many files in a GitHub repo? ####
Speaking of overall content length of the repo, it is crucial to understand 
the input tokens limits for OpenAI models used in the project.
After that, it is important to chunk the content of the repo, so that every chunk 
is described and reviewed properly according to the given structure.
When separate chunks are summarized, a summary for the whole repo can be created and
can be used for review along with repo structure
