<!-- FILEPATH: /Users/ashwinprasanth/Documents/Coding/dev-team-task/src/routes/NewsCard.svelte -->
<!-- News card element - would contain image (if exists), title and source -->
<!-- On clicking the element, it would open a pop-up like window with more text (maybe summarised) along with a link to read more -->

<script lang="ts">
    
    import './styles.css';
    import default_news from './default-news.png';
    
    import { scale,fade } from 'svelte/transition';
    
    
    export let title: string;
    export let source: string;
    export let image: string;
    export let description: string;
    export let sourceUrl: string;
    
    let isModalOpen = false;

    const openModal = () => { 
        isModalOpen = true;
    };

    const closeModal = () => {
        isModalOpen = false;
    };

    const stripTitle = (title: string) => {
        // remove leading and trailing spaces
        title = title.trim();
        // try splitting based on "|"
        const titleSplit = title.split('|');
        if (titleSplit.length > 1) {
            return titleSplit[0];
        }
        else{
            // try splitting based on "-"
            const titleSplit = title.split('-');
            if (titleSplit.length > 1) {
                return titleSplit.slice(0, -1).join('-');
            }
        }
    };

</script>

<div class="news-card" tabindex="0" on:click={openModal} on:keydown|preventDefault={e => e.key === 'Enter' && openModal()} role="button" aria-label="Open news article">
    <img class="news-card-image" src={image || default_news} alt={default_news}/>
    <div class="news-card-text">
        <h3 class="news-title">{stripTitle(title)}</h3>
        <p class="news-card-source">{source}</p>
    </div>
</div>

{#if isModalOpen}
    <div class="modal" id="news-modal" in:fade>
        <div class="modal-content" in:scale>
            <h3>{stripTitle(title)}</h3>
            <img src={image || default_news} alt={default_news}/>
            {#if description}
                <p>{description}</p>
            {/if}
            <a href="{sourceUrl}" target="_blank" class="read-more-link">See More</a>
            <button class="close-modal-button" on:click={closeModal}>&larr; Back</button>
        </div>
    </div>
{/if}

<style>

    .modal {
        position: fixed;
        top: 0; 
        left: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1000;
        width: 100%;
        height: 100%;
        background-color: rgba(0,0,0,0.4);
    }

    .modal-content {
        background-color: white;
        border-radius: 20px;
        overflow-y: auto;
        /* define width and height based on size of screen */
        width: 70%;
        height: 90%;
        padding: 20px;
        box-shadow: 0px 0px 5px 0px rgba(0,0,0,0.2);
        /* center allign all the items */
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .modal-content img {
        width: 70%;
        height: 70%;
        margin-bottom: 20px;
    }

    .close-modal-button {
        margin-top: 10px;
        padding: 5px 10px;
        border-radius: 5px;
        background-color: #f2f2f2;
        border: 1px solid #ccc;
        cursor: pointer;
        color: #fff;
        background-image: linear-gradient(to right, #2697ff 0%, #62b2fc 100%);
        transition: all 0.2s ease-in-out;
    }

    .close-modal-button:hover {
        background-position: right center;
    }

    .read-more-link {
        display: block;
        margin-top: 10px;
        padding: 10px 20px;
        border-radius: 20px;
        background-image: linear-gradient(to left, #65b3fc 0%, #0c84f3 100%);
        color: white;
        font-weight: 600;
        text-align: center;
        text-decoration: none;
        transition: all 0.2s ease-in-out;
    }

    .read-more-link:hover {
        background-position: right center;
    }
    
    .news-card {
        display: inline-block;
        width: 30%;
        margin: 1%;
        box-shadow: 0px 0px 5px 0px rgba(0,0,0,0.2);
        border-radius: 10px;
        overflow: hidden;
        vertical-align: top;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        cursor: pointer;
    }

    .news-card-image {
        width: 300px; 
        height: 200px;
    }

    .news-card-text {
        padding: 10px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        height: 100%;
    }

    .news-card-text h3 {
        text-align: left;
        margin-top: 0;
    }

    .news-card-text p {
        text-align: right;
        margin-bottom: 0;
    }

    .news-card-source {
        font-style: italic;
        font-size: 0.8rem;
    }

    @media (max-width: 768px) {
        .news-card {
            width: 45%;
        }
    }

    @media (max-width: 576px) {
        .news-card {
            width: 100%;
        }
    }
</style>