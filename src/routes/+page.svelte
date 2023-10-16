<script lang="ts">
    import './styles.css';
    import NewsCard from './NewsCard.svelte';
    import 'iconify-icon'
    import { onMount } from 'svelte';
    import Fuse from 'fuse.js';
    import countries  from '../countries.json';

    interface NewsItem {
        title: string;
        description: string;
        publishedAt: string;
        imgSrc: string;
        source: string;
        url: string;
        country: string;
    }

    let news: NewsItem[] = [];

    let fuse = new Fuse([], {
        keys: [],
    });

    let searched = false;
    
    // fetch news using API
    const fetchNews = async () => {
        const response = await fetch('http://127.0.0.1:5000/fetch-news');
        if (response.ok) {
            console.log('Fetched news using NewsAPI');
        } else {
            console.error('Failed to fetch news using NewsAPI:', response.status);
        }
    };

    // get news from db
    const getNews = async () => {
        const response = await fetch('http://127.0.0.1:5000/get-news'); 
        if (response.ok) {
            news = await response.json();
            console.log('Got news from DB');

            filteredNews = news;
            fuse = new Fuse(filteredNews, {
                keys: ["title", "description", "source"],
                threshold: 0.3,
            }); 
            console.log("filtered news inside getnews: ", filteredNews)

        } else {
            console.error('Failed to get news from DB:', response.status);
        }
    };

    let searchText = '';
    let filteredNews: NewsItem[] = news;
    let searchResults: NewsItem[]= news;

    const handleCountryChange = (event: any) => {;
        const country = event.target.value;
        console.log(country)
        if (country === 'all') {
            filteredNews = news;
            fuse = new Fuse(filteredNews, {
                keys: ["title", "description", "source"],
                threshold: 0.3,
            }); 
        }
        else {
            filteredNews = news.filter((newsItem) => newsItem.country === country);
            fuse = new Fuse(filteredNews, {
                keys: ["title", "description", "source"],
                threshold: 0.3,
            }); 
            console.log(filteredNews)
        }
    };

    const handleSearch = (event: any) => {
        searched = true;
        searchText = event.target.value;
        if (searchText === '') {
            searched = false;
        } else {
            searchResults = fuse.search(searchText).map((result) => result.item);
        }
    };

    


    onMount(() => {
        getNews();

        // Schedule the functions to run every 15 minutes
        const intervalId = setInterval(() => {
            fetchNews();
        }, 15 * 60 * 1000);

        // Clear the interval when the component is destroyed
        return () => clearInterval(intervalId);
    });
</script>

<h1>NewsApp</h1>
<h2>The news forum of tomorrow</h2>

<!-- Search and filtering options -->
<!-- Add a search bar -->
<div class="options-bar">
    <div class="search-container">
        <div class="search">
            <input type="text" class="searchTerm" placeholder="Search for news..." on:input={handleSearch}>
            <button type="submit" class="searchButton">
                <iconify-icon icon="ic:outline-search"></iconify-icon>
            </button>
        </div>
    </div>
    <div class="country-filter-container">
        <select name="country" id="country" class="country-filter" on:change={handleCountryChange}>
            <option value="all">All countries</option>
            {#each Object.keys(countries) as country}
            <option value={country}>{countries[country]}</option>
            {/each}
        </select>
    </div>
</div>

<!-- Newscard section -->
<div class="news-card-container">
    <!-- if user hasn't searched yet, then show all news -->
    {#if !searched}
        {#each filteredNews as newsItem}
            <NewsCard 
                title={newsItem.title} 
                source={newsItem.source} 
                image={newsItem.imgSrc}
                description={newsItem.description}
                sourceUrl={newsItem.url}
            />
        {/each}
    {/if}
    <!-- if user has searched, then show search results -->
    {#if searched && searchResults.length > 0}
        {#each searchResults as newsItem}
            <NewsCard 
                title={newsItem.title} 
                source={newsItem.source} 
                image={newsItem.imgSrc}
                description={newsItem.description}
                sourceUrl={newsItem.url}
            />
        {/each}
    {/if}
    <!-- No results => show error -->
    {#if searched && searchResults.length === 0}
        <h2>No results found :/</h2>
    {/if}
</div>


<style>

    .options-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem;
        padding-bottom: 0;
    }

    
    .search-container {
        padding: 1rem;
        flex-grow: 1;
    }

    .country-filter-container {
        padding: 1rem;
        order: 1;
    }

    .country-filter {
        padding: 0.5rem;
        font-size: 1rem;
        border-radius: 0.25rem;
        border: 1px solid var(--color-theme-1);
        background-image: linear-gradient(to left, var(--color-bg-0), var(--color-bg-2));
        color: black;
        outline: none;
        margin-right: 1rem;
        cursor: pointer;
        transition: all 0.2s ease-in-out;
    }

    .country-filter:hover {
        background-color: white;
        color: var(--color-theme-1);
    }

    .search {
        width: 100%;
        position: relative;
        display: flex;
    }

    .searchTerm {
        width: 100%;
        border: 1px solid var(--color-theme-1);
        background-image: linear-gradient(to right, var(--color-bg-0), var(--color-bg-2));
        /* color: black; */
        border-right: none;
        padding: 5px;
        height: 24px;
        border-radius: 5px 0 0 5px;
        outline: none;
    }

    .searchTerm:focus{
        color:black;
    }

    .searchButton {
        width: 40px;
        height: 36px;
        border: 1px solid var(--color-theme-1);
        background: var(--color-theme-1);
        text-align: center;
        color: #fff;
        border-radius: 0 5px 5px 0;
        cursor: pointer;
        font-size: 20px;    
    }

    .news-card-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center; 
    }

    h1 {
        padding: 1rem;
        padding-bottom: 0;
        text-align: center; 
        margin: 0;
    }

    h2 {
        padding: 1rem;
        padding-top: 0;
        text-align: center;
        margin: 0;
    }
</style>