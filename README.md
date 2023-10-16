# NewsApp - Inter IIT Tech Meet 12.0 - IIT KGP Development Team Selection Task

## Demonstration


https://github.com/ashwinpra/newsforum-dev-task/assets/62993493/281d8f86-7d99-47f3-a3d6-7d3c4e14d5b2





## How to Run Locally? 
### Using Docker
> ⚠️ I have not been able to implement dockerization properly, so this will not work, kindly proceed [here](https://github.com/ashwinpra/newsforum-dev-task/edit/main/README.md#without-docker)
- Clone the repository
- Navigate to the root directory
- Run `docker-compose up`
- Navigate to `localhost:5173` to view the app

### Without Docker
   - Clone the repository
   #### Setting up the backend 
   - Navigate to `server/` directory
   - Optional, but recommended: Create a virtual environment using `python3 -m venv venv` or `virtualenv venv`
   - Activate the virtual environment using `source venv/bin/activate`
   - Run `pip install -r requirements.txt` to install all the dependencies
   - Create a `.env` file in the `server/` directory and add the following environment variable:
     - `NEWS_API_KEY` : Your News API key - Get it from [here](https://newsapi.org/)
   - Run `flask run` to start the server
       
   #### Setting up the frontend
   - Navigate to the root directory
   - Run `npm install` to install all the dependencies
   - Run `npm run dev` to start the frontend server

   - Navigate to `localhost:5173` to view the app

## Problem Statement 

- Clean and responsive front-end
- Should contain a search bar for headlines and keywords
- A news entity should have the following features:
    - Headline
    - Content
    - Image
    - Video (playback optional)
- Real time news feed
    - Extensive web scraping is not required. Simply ensure that the coming feed conveys a sense of freshness.
- Filtering options for
    - Geographic location
    - Topics (eg. Sports, Politics, Technology, Finance etc.)
- Newsletter subscription service
    - Email can be stored in your choice of database or data-structure

## Features that *could not* be implemented 
- Video in news entity
  - The news API used does not provide video content
- Topicwise filtering 
  - Since the news API is on the free tier, it is limited to 100 hits per day, and I already exhausted it by doing a lot of testing, so the topicwise filtering could not be implemented, although country-wise filtering was implemented
- Newsletter subscription service 
  - Could not implement this due to time constraints and inexperience
- Dockerization/Deployment
  - Due to time constraints and inexperience
