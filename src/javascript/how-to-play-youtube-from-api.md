
date: None
author(s): None

# [How To Get YouTube Playlist Contents from the YouTube Data API - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/javascript/how-to-get-youtube-playlist-contents-from-the-youtube-data-api)

_This is the first part of our series on[How to Develop With the YouTube Data API](https://www.programmableweb.com/api-university/how-to-develop-youtube-data-api). In this part we provide an overview of the API and the developer portal, and show you how to build an app that returns the contents of a publicly viewable YouTube playlist._

The [YouTube Data API](https://www.programmableweb.com/api/youtube-data)[Track this API](https://www.programmableweb.com/user/register?destination=node/207025&pwaction=track&pwentity=node&pwtrack=143332&pwflag=follow_api), currently in version 3, gives developers the ability to add a number of YouTube features to their applications. The API can be used to upload and search for videos, manage playlists and subscriptions, update channel settings and more.

The API gives you access to nearly 20 different resources and supports common HTTP verbs such as GET (list), POST (insert), PUT (update), and DELETE (delete) for each resource type. The chart below shows which operations are supported across the different resources.

![Figure 1: List of supported API operations](https://www.programmableweb.com/sites/default/files/get-playlist-contents-youtube-data-api-figure-01-supported-api-operations.png)


Figure 1: List of supported API operations.

Developers need to register their applications and obtain access before using the API. There are two types of access - simple and authorized. If you want to search for publicly available videos and playlists, then simple access via an API key is all that you need. For applications that take actions on behalf of the user such as uploading videos, editing playlists or anything that would require a user to be logged in, authorized access using an OAuth 2.0 workflow is required. With over a billion users and nearly 5 billion videos watched daily, YouTube has a vast collection of data to explore, much of it publicly available. I wanted to learn about the API and how I could use it to access this data.

## Getting Started with the Portal

The first step was to head over to the [YouTube developer portal](https://developers.google.com/youtube/). I've seen plenty of portals and YouTube's follows the best practice of laying out the various APIs available (see figure 2) and telling the user in clear language what can be accomplished with each, be it playing videos, exploring the platform's data, understanding user behavior and more.

![Figure 2: The YouTube developer portal home page clearly shows the available APIs and what can be done with each](https://www.programmableweb.com/sites/default/files/get-playlist-contents-youtube-data-api-figure-02-youtube-developer-portal.png)


Figure 2: The YouTube developer portal home page clearly shows the available APIs and what can be done with each.

My interest was in using YouTube data so I clicked through to the overview link; this is where I had my first bit of confusion. I was taken to the Overview page as expected and it does a good job of explaining, in detail, what the API is about and the basics of how it works. According to the navigation menu at the top, I was in the Guides section of the developer portal.

![Figure 3: YouTube Data API Overview Page](https://www.programmableweb.com/sites/default/files/get-playlist-contents-youtube-data-api-figure-03-youtubedata-api-overview.png)


Figure 3: YouTube Data API Overview Page.

Clicking the navigational link for Home took me to [a landing page](https://developers.google.com/youtube/v3/) for the YouTube Data API (according to the breadcrumbs) that looks strikingly similar to the YouTube developer landing page that was shown in Figure 2. But they're different. From there, when I click the Get Started link, it puts me back to the previously mentioned Overview page. Or, from that landing page, you can click a link for an Implementation Guide which also takes me to an Overview page, but one that's different from the first one I encountered ([this one](https://developers.google.com/youtube/v3/guides/implementation) is for an "Implementation and Migration Guide"). Lastly, from the YouTube Data API landing page, I can also click the Supported Features link which takes me to the [search: list method](https://developers.google.com/youtube/v3/docs/search/list) within the Reference section. This "list method" page is not titled "Supported Features" nor is really a narrative about the Data API's search capability. Its a reference page that starts with an embedded execution environment (for testing of several use cases across a variety of languages) after which appears a laundry list of myriad different parameters that can be used when calling the API.

This confusing labyrinth of pages and terminology is one of my pet peeves with the documentation across a number of Google's APIs; there is often so much information being packed into a single portal, and the links take you in and out of sections in a way that feels like you are skipping around instead of hierarchically exploring the site. I found myself at times unsure of where I just came from and this gave me a disjointed feeling instead of a smooth experience where I'm progressing through a journey of logically sequenced pages. To be fair, this issue is not unique to YouTube or Google. We've observed it in many of the developer portals that we study.

I eventually made my way back to the Overview page and the section that explains what needs to happen before getting started. A video showing the steps is also included but it is out of date as the workflow being shown no longer matches the workflow the site takes you through. In truth, the video isn't necessary. This part was straightforward and the UX for setting up my project, registering it to use the Data API and requesting my API key was very good, allowing me to be ready within a couple of minutes. As mentioned above, one of the steps while obtaining credentials is to decide on the level of access your application needs. For the purposes of this project, I chose simple access which requires only an API key.

![Figure 4: Choosing the right credentials for your application](https://www.programmableweb.com/sites/default/files/get-playlist-contents-youtube-data-api-figure-04-choosing-the-right-credentials.png)


Figure 4: Choosing the right credentials for your application.

## Diving Into the Documentation

Before diving full on into the API documentation, I had to decide what the first iteration of my code should accomplish. Just to get my feet wet with the YouTube Data API, I decided that a developer should be able to provide the ID of any YouTube playlist and in return, a web page would load a linked-list of videos from that playlist. So, for the purposes of this article, I will hardcode some of the data (the playlist title and ID) to keep the code to a more digestible sample. The goal of this article is to give you a sense of what the API can accomplish. In a later article, I will flesh out the application in such a way that the it reflects a more realistic use case; one that discovers and displays all the playlists associated with a specific YouTube username.

At this point it was time to start looking through the API documentation, and this is where I encountered my first stumbling block. Keeping in mind my goal of displaying a linked list of videos from one of my YouTube playlists, the [API Portal landing page](https://developers.google.com/youtube/v3/) includes a section about searching for content. I clicked the link for supported features and, as mentioned earlier was immediately taken a couple of levels deep into the API reference (the [search: list resource](https://developers.google.com/youtube/v3/docs/search/list)). I found the inconsistencies in page layout to be jarring, requiring me to reorient myself. The issue is that there is a lot of information that Google is trying to organize with a limited amount of space in which to do so. In the figure below, you can see the two-menu system Google uses on some of its pages (menus on the left and right).

![Figure 5: API reference page showing right and left menus](https://www.programmableweb.com/sites/default/files/get-playlist-contents-youtube-data-api-figure-05-api-reference-page.png)


Figure 5: API reference page showing right and left menus.

For a more experienced developer, wading through the documentation in this way may be a breeze. But, I found it to be a barrier to quickly getting to the "Hello World" version of my idea. I'm still green when it comes to coding so I was looking for a bit more hand-holding to get me to my final goal. Google does try to make things easier by including code snippets for each resource as shown below.


    // Sample js code for playlistItems.list
    // See full sample for buildApiRequest() code, which is not
    // specific to a particular API or API method.
    buildApiRequest('GET',
                    '/youtube/v3/playlistItems',
                    {'maxResults': '25',
                     'part': 'snippet,contentDetails',
                     'playlistId': 'PLBCF2DAC6FFB574DE'});

However, this code alone doesn't do anything when placed into your application. Instead, if you want Google's sample code, you have to copy and paste a large chunk of boilerplate code (that is hidden by default) in order for the code to work. Google created this boilerplate so that the same code can be reused across many of its APIs. While this makes things easier for the Google employee who must document the APIs, it doesn't really help the developer. Instead it introduces a lot of overhead that unnecessarily bloats your "Hello World" code, not to mention the obstruction it creates to learning the basics of working with the API.

Another example of the disjointed nature of the documentation is when you are working with the part parameter on API requests. The part parameter specifies a comma-separated list of resource properties that the API response can include at the option of the develper. This was a key piece needed to structure my requests order to properly work with the API. You can see in figure 6 below how Google documents this in its API reference (eg: [the reference](https://developers.google.com/youtube/v3/docs/playlists/list) for retrieving a list of playlists associated with a YouTube channel).

![Figure 6: The part parameter on one of the API resources without a clear definition for what is contained within each part name](https://www.programmableweb.com/sites/default/files/get-playlist-contents-youtube-data-api-figure-06-part-parameter.png)


Figure 6: The part parameter on one of the API resources without a clear definition for what is contained within each part name.

As you can see, there isn't a clear explanation of what the various part names consist of (or any links to other pages where these parts might be explained). I could guess at what would be contained in parts such as contentDetails or id, but the only way I knew for sure was to use Javascript's console.log() while testing my code to discover it for myself. In fact, I was able to find examples that showed the data returned for various part parameters. For example, the [PlaylistItems resource overview page](https://developers.google.com/youtube/v3/docs/playlistItems) shows a JSON representation of a playlistItem that includes the data I had been searching for (see figure 7 below).

![Figure 7: JSON representation of the PlaylistItems resource showing what data can be expected from the various part parameters](https://www.programmableweb.com/sites/default/files/get-playlist-contents-youtube-data-api-figure-07-json-representation-playlistItems-resource.png)


Figure 7: JSON representation of the PlaylistItems resource showing what data can be expected from the various part parameters.

This pointed to a lack of cohesive organization of the portal; the ideal place to include this information would be on the pages where the parts are mentioned . Here the information is given the greatest context for someone trying to understand the API. If it didn't make sense to include the representation on each of those pages, perhaps as a means to reduce redundancy, at least it would have been helpful to have linked the part names back to the single representation. Again, the problem wasn't that the information didn't exist, it was that it wasn't always in places that were contextually relevant.

With these organizational issues in mind, this is where Google could have offered a couple of brief tutorials that take users step by step through the process of setting up a simple "Hello World" application that calls the API. The tutorials don't have to be exhaustive but they should take the reader through the minimally viable steps of calling the API so that you have a better understanding of how the requests and responses work.

I decided that I would have better luck turning to, ironically enough, a YouTube video. One of the bonuses from working with APIs from the larger providers, like Google, is that many of them have third-party produced tutorials and walkthroughs available on the web. A quick search on YouTube pulled up the video below. It uses JavaScript and jQuery to list the videos on a YouTube channel which is what I was looking to accomplish.

After watching the video to make sure that it did what I wanted, I made some adjustments, substituted my information and gave it a try. As mentioned earlier, I wanted to keep my first iteration of this code simple and to do that, my code assumes that you already have the ID of the playlist you want to retrieve. Finding the ID of a playlist is pretty easy. Point your browser to any YouTube channel that has one or more playlists, right click on a playlist link, and pick Copy Link Address from the pop up menu. This will copy the entire playlist link to your clipboard. Paste the link into a text editor (or any place that will let you paste the contents of your clipboard). The link will look something like this:


    https://www.youtube.com/watch?v=NNM2kEBGiRs&list=PLfHByg2esTuIuuHC2rLY7aCCP0yKn9622

The playlist ID is the string of letters and digits that comes after the "list=" parameter.

I hard-coded that playlist ID into the first iteration of my code. One other thing to note about JSBin (the interactive code editor that's embedded at the top of this tutorial) is that you can hide your API key. As a best practice, you never want to reveal your API key in your application's source code. We have publsihed a technique (covered in this [article on _ProgramableWeb_](https://www.programmableweb.com/news/how-to-hide-api-keys-html5-storage-public-code-samples/how-to/2018/01/17)) that lets you prompt the user for his or her API after which it stores that key in HTML5 storage. As you can see from the Bin embedded above, my code makes use of this technique.

One YouTube Data API inconvenience that developers and API designers can learn from has to do with the how the API does not respond with complete URLs for assets that the developer might want to link to. For example, a video. Instead, for every asset that gets included in an API response, the API only responds with an asset ID. If you want to link to that asset, you have to know something about YouTube's URL structure and then, with the asset ID in hand, construct the hyperlink with your code. For example, YouTube's URL for linking to a video is:


    https://www.youtube.com/watch?v=NNM2kEBGiRs

where "NNM2kEBGiRs" is the asset ID of the video.

Since the YouTube Data API only responds with IDs, you as the developer must know to concatenate an ID with "<https://www.youtube.com/watch?v=>" in order to craft the entire hyperlink.

This design, where developers must hard code URL fragments into their source code, makes for poorly performing or worse, easily broken applications. If YouTube decides to change its URL structure (which it has already done in the past), at best, it will redirect legacy structured URLs to the right place. At worst, it might do nothing and applications could break as a result.

One could argue that by returning the asset ID as opposed to the entire URL, YouTube is ensuring smaller payloads. But in our opinion, the risk of application breakage down the line isn't worth the small savings.

## What Else Was In the Portal

One thing I appreciated about the portal was the ability to test out calls directly within the documentation (see figure 8 below). Once I came back to the portal after having finished the video tutorial, calling the API from within the docs was helpful for understanding what I could expect when making requests.

![Figure 8: Example call made directly within the documentation](https://www.programmableweb.com/sites/default/files/get-playlist-contents-youtube-data-api-figure-08-example-call.png)


Figure 8: Example call made directly within the documentation.

There is also a separate [console](https://developers.google.com/apis-explorer/#p/youtube/v3/) which allows you to execute requests without needing to authorize with OAuth. Due to the large number of resources in this API, the console is handy once you have narrowed in on the calls you want to make.

Another great feature that I found later was the [Sample Code section](https://developers.google.com/youtube/v3/code_samples/). Here you can find nine groupings of code samples covering eight languages. Some languages such as Python have nearly two dozen examples while others such as .NET are limited to just a handful. In the absence of basic "Hello World" style walkthroughs, these collections of code are a good place for someone new to the API to start.

The YouTube Data API does have a number of SDKs to use, but the portal landing page doesn't make this readily apparent. From the API landing page, there is a section labeled Other Resources, but clicking through the various links did not turn up anything useful. The [YouTube GitHub](https://github.com/youtube) page is also lacking any mention of SDKs. You have to go back to the API overview page to find a link to the [SDK page](https://developers.google.com/youtube/v3/libraries) called "Client Libraries." Here there are links for official clients in six languages including Java, JavaScript, .NET, Objective-C, PHP and Python as well as early stage SDKs for Dart, Go, Node.js and Ruby.

## Summary

Overall this is a good API that offers developers a lot of options to include YouTube functionality into their applications. The portal itself is deep and has nearly everything a developer would look for when using the API for the first time. I only have two gripes. First, as a new developer, I would have appreciated a basic tutorial or two that got me from point A to "Hello World" in a reasonable amount of time. "Time to Hello World" is a metric that many API providers use to gauge the quality of their developer portals. I was lucky that due to the popularity of the API that I could turn to a third party resource. But it seems like a missed opportunity to make the developer experience that much better. My other complaint is that while the portal is deep, at times it can feel a bit unstructured. It isn't easy to synthesize the amount of information contained here, but there are a number of places where more careful organization of the site can help take developers on a journey instead of throwing them in the middle of the ocean.

 _This is the first part of our series on[How to Develop With the YouTube Data API](https://www.programmableweb.com/api-university/how-to-develop-youtube-data-api). In [part two](https://www.programmableweb.com/news/how-to-discover-playlist-ids-youtube-data-api/how-to/2018/04/17) we show you how to show all of a channel's playlists programmatically by only knowing the channel ID. Using this, you can query the YouTube Data API in order to discover all the playlist IDs._
