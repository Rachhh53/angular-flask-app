import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { Observable, throwError, from } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';
//import 'rxjs/add/operator/catch';
import { API_URL } from './env';
//import {Exam} from './exam.model';

@Injectable()
export class BigqueryApiService {

    constructor(private http: HttpClient) {
    }

    private static _handleError(err: HttpErrorResponse | any) {
        return throwError(() => err.message || 'Error: Unable to complete request.');
    }

/*     getResults(): Observable<any> {
        return from(
          fetch(
            `${API_URL}`, // the url you are trying to access
            {
              headers: {
                'Content-Type': 'application/json',
              },
              method: 'GET', // GET, POST, PUT, DELETE
              mode: 'no-cors' // the most important option
            }
          ));
      } */
      getResults() : Observable<any> {
        return this.http
          .get(`${API_URL}/`)
          // .catch(BigqueryApiService._handleError)
          .pipe(
            catchError(BigqueryApiService._handleError)
          )
      }

}