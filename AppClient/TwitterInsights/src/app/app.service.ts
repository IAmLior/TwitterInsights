import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AppService {

  constructor(private http: HttpClient) { }

  postData(data: any): Observable<any> {
    const url = '';
    return this.http.post<any>(url, data);
  }
}
