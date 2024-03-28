import { Component } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { AppService } from './app.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {

  public form: FormGroup;
  public data: any = null;
  public totalItems: number = 0

  constructor(private formBuilder: FormBuilder,
              private appService: AppService) {
    this.form = this.formBuilder.group({
      tokens: [],
      tweet: []
    });
  }

  getInsights() {
    const tokensStr = this.form.controls['tokens'].value as string;
    const tokensArray = tokensStr.split(',').map(token => token.trim()).filter(Boolean);

    this.appService.getInsights(tokensArray).subscribe(response => {

        console.log('Response from server:', response);
        const topicCounts: { [key: string]: number } = {}; 
        const topics = response.result.flat();
        topics.forEach((topic: string) => {
          topic = topic.toLocaleUpperCase()
          topicCounts[topic] = topicCounts[topic] ? topicCounts[topic] + 1 : 1; 
        });
        const data = Object.keys(topicCounts).map(key => {
          return { name: key, value: topicCounts[key] };
        });
        console.log(data);
        data.sort((a: { name: string, value: number } , b: { name: string, value: number }) => b.value - a.value);
        
        const totalItems = response.result.length;
        this.data = data.slice(0,10);
        this.totalItems = totalItems;
    }, error => {
        console.error('Error:', error);

        const mockResponse = {
          "result": [
            [
              "Music",
              "Celebrities",
              "Entertainment"
            ],
            [
              "Art",
              "Photography",
              "Culture"
            ],
            [
              "Sports",
              "Entertainment",
              "NBA"
            ],
            [
              "Music",
              "Celebrities",
              "Pop"
            ],
            [
              "Music",
              "Celebrities",
              "Pop"
            ],
            [
              "Music",
              "Events",
              "Concerts"
            ],
            [
              "Politics",
              "Music",
              "Celebrities"
            ],
            [
              "Politics",
              "Contests",
              "Music"
            ],
            [
              "Music",
              "Events",
              "Concerts"
            ],
            [
              "Contests",
              "Travel",
              "Music"
            ],
            [
              "Music",
              "Events",
              "Entertainment"
            ],
            [
              "Music",
              "Events",
              "Entertainment"
            ],
            [
              "Music",
              "Events",
              "Entertainment"
            ],
            [
              "Politics",
              "News",
              "Obituary"
            ],
            [
              "Politics",
              "News",
              "Obituary"
            ],
            [
              "Music",
              "Artists",
              "Culture"
            ],
            [
              "Music",
              "Artists",
              "Sports"
            ],
            [
              "Music",
              "Artists",
              "Inspiration"
            ],
            [
              "Photography",
              "Fashion",
              "Art"
            ],
            [
              "Film",
              "Collaborations",
              "Inspiration"
            ],
            [
              "music",
              "movies",
              "film"
            ],
            [
              "sports",
              "basketball",
              "NBA"
            ],
            [
              "movies",
              "film",
              "celebrity"
            ],
            [
              "sports",
              "college football",
              "cancer"
            ],
            [
              "movies",
              "film",
              "James Bond"
            ],
            [
              "sports",
              "basketball",
              "NBA"
            ],
            [
              "sports",
              "basketball",
              "NBA"
            ],
            [
              "movies",
              "film",
              "James Bond"
            ],
            [
              "music",
              "movies",
              "film"
            ],
            [
              "sports",
              "basketball",
              "NBA"
            ],
            [
              "Sports",
              "NBA",
              "Lebron James"
            ],
            [
              "Sports",
              "NBA",
              "Lebron James"
            ],
            [
              "Sports",
              "NBA",
              "Lebron James"
            ],
            [
              "Sports",
              "NBA",
              "Lebron James"
            ],
            [
              "Sports",
              "NBA",
              "Lebron James"
            ],
            [
              "Sad News",
              "James Gandolfini",
              "RIP"
            ],
            [
              "Music",
              "James Fauntleroy",
              "Album"
            ],
            [
              "Music",
              "Carole King",
              "James Taylor"
            ],
            [
              "Sports",
              "NBA",
              "Lebron James"
            ],
            [
              "Sports",
              "NBA",
              "Lebron James"
            ],
            [
              "Sports",
              "Entertainment",
              "Politics"
            ],
            [
              "Sports",
              "Entertainment",
              "Politics"
            ],
            [
              "Art",
              "Fashion",
              "Entertainment"
            ],
            [
              "Fashion",
              "Art",
              "Entertainment"
            ],
            [
              "Sports",
              "Entertainment",
              "Politics"
            ],
            [
              "Sports",
              "Entertainment",
              "Politics"
            ],
            [
              "Entertainment",
              "Politics",
              "Sports"
            ],
            [
              "Politics",
              "Sports",
              "Entertainment"
            ],
            [
              "Politics",
              "Sports",
              "Entertainment"
            ],
            [
              "Politics",
              "Sports",
              "Entertainment"
            ],
            [
              "entertainment",
              "media",
              "tv"
            ],
            [
              "politics",
              "military",
              "government"
            ],
            [
              "politics",
              "government",
              "security"
            ],
            [
              "crime",
              "law",
              "police"
            ],
            [
              "sports",
              "crime",
              "basketball"
            ],
            [
              "sports",
              "crime",
              "basketball"
            ],
            [
              "sports",
              "social issues",
              "drugs"
            ],
            [
              "sports",
              "business",
              "nba"
            ],
            [
              "social issues",
              "politics",
              "discrimination"
            ],
            [
              "entertainment",
              "media",
              "tv"
            ],
            [
              "Entertainment",
              "TV",
              "Late Night TV"
            ],
            [
              "Entertainment",
              "TV",
              "Late Night TV"
            ],
            [
              "Entertainment",
              "TV",
              "Late Night TV"
            ],
            [
              "Entertainment",
              "TV",
              "Late Night TV"
            ],
            [
              "Entertainment",
              "TV",
              "Late Night TV"
            ],
            [
              "Entertainment",
              "Pop Culture",
              "Humor"
            ],
            [
              "Entertainment",
              "Pop Culture",
              "Humor"
            ],
            [
              "Entertainment",
              "TV",
              "Late Night TV"
            ],
            [
              "Entertainment",
              "TV",
              "Late Night TV"
            ],
            [
              "Entertainment",
              "TV",
              "Late Night TV"
            ],
            [
              "Entertainment",
              "Comedy",
              "Fallon Show"
            ],
            [
              "Entertainment",
              "Comedy",
              "Fallon Show"
            ],
            [
              "Entertainment",
              "Comedy",
              "Fallon Show"
            ],
            [
              "Entertainment",
              "Comedy",
              "Pets"
            ],
            [
              "Entertainment",
              "Comedy",
              "Fallon Show"
            ],
            [
              "Entertainment",
              "Music",
              "Nature"
            ],
            [
              "Sports",
              "Basketball",
              "NBA"
            ],
            [
              "Sports",
              "Basketball",
              "Humor"
            ],
            [
              "Entertainment",
              "Comedy",
              "Fallon Show"
            ],
            [
              "Sports",
              "Basketball",
              "College"
            ],
            [
              "Celebrity",
              "Music",
              "Sports"
            ],
            [
              "Celebrity",
              "Sports",
              "Talk Shows"
            ],
            [
              "Celebrity",
              "Music",
              "Talk Shows"
            ],
            [
              "Celebrity",
              "Music",
              "Talk Shows"
            ],
            [
              "Celebrity",
              "Music",
              "Talk Shows"
            ],
            [
              "Celebrity",
              "Sports",
              "Talk Shows"
            ],
            [
              "Celebrity",
              "Talk Shows"
            ],
            [
              "Celebrity",
              "Music",
              "Talk Shows"
            ],
            [
              "Celebrity",
              "Sports"
            ],
            [
              "Celebrity",
              "Sports"
            ],
            [
              "Photography",
              "Sports",
              "Culture"
            ],
            [
              "Photography",
              "Travel",
              "Aviation"
            ]
          ]
        }
        const topicCounts: { [key: string]: number } = {}; 
        const topics = mockResponse.result.flat();
        topics.forEach((topic: string) => {
          topic = topic.toLocaleUpperCase()
          topicCounts[topic] = topicCounts[topic] ? topicCounts[topic] + 1 : 1; 
        });
        const data = Object.keys(topicCounts).map(key => {
          return { name: key, value: topicCounts[key] };
        });
        console.log(data);
        data.sort((a: { name: string, value: number } , b: { name: string, value: number }) => b.value - a.value);
        
        const totalItems = mockResponse.result.length;
        this.data = data.slice(0,10);
        this.totalItems = totalItems;
    })
  }

  postTweet() {
    const tweetStr = this.form.controls['tweet'].value as string;
    this.appService.postTweet(tweetStr).subscribe(response => {
      console.log('Response from server:', response);
    }, error => {
      console.error('Error:', error);
    })
  }

}
