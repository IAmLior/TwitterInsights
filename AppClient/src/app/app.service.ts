import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AppService {

  constructor(private http: HttpClient) { }

  getInsights(tokensArr: string[]): Observable<any> {
    const url = 'http://api-app.minikube.local/app/getInsights/';
    let params = new HttpParams();
    tokensArr.forEach(token => {
      params = params.append('tokens', token);
    });

    return this.http.get<any>(url, {params});
  }

  postTweet(tweet: string): Observable<any> {
    const url = 'http://api-app.minikube.local/app/postTweet/';
    let params = new HttpParams();
    params = params.append('text', tweet);
    return this.http.post<any>(url, null, {params});
  }
}
