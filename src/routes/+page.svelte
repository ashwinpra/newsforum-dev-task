<script lang="ts">
    import './styles.css';
    import NewsCard from './NewsCard.svelte';

    import { onMount } from 'svelte';

    interface NewsItem {
        title: string;
        description: string;
        imgSrc: string;
        source: string;
        url: string;
    }

    let news: NewsItem[] = [];

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
            console.log(news)
        } else {
            console.error('Failed to get news from DB:', response.status);
        }
    };

    onMount(() => {
        // Run the functions initially
        fetchNews();
        getNews();

        // Schedule the functions to run every 15 minutes
        const intervalId = setInterval(() => {
            fetchNews();
            getNews();
        }, 15 * 60 * 1000);

        // Clear the interval when the component is destroyed
        return () => clearInterval(intervalId);
    });
</script>

<h1>NewsApp</h1>
<h2>The news forum of tomorrow</h2>

<!-- Search and filtering options -->


<!-- Newscard section -->
<div class="news-card-container">
    {#each news as newsItem}
        <NewsCard 
            title={newsItem.title} 
            source={newsItem.source} 
            image={newsItem.imgSrc}
            description={newsItem.description}
            sourceUrl={newsItem.url}
        />
    {/each}
</div>


<style>

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