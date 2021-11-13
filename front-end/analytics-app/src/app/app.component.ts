import { Component } from '@angular/core';
import { Subscription } from 'rxjs';
import { BigqueryApiService } from './bigquery-api.service'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'analytics-app';
  predictions!: Subscription;
  clusters!: any;

  constructor(private bigqueryApi: BigqueryApiService) {}

  ngOnInit() {
    const myObserver = {
      next: (res: any) => {console.log('Observer got a next value: ' + res), 
   /*    res.replace('"\\"','')
      res.replace('\\""','') */
      this.clusters = res
    },
      error: (err: Error) => console.error('Observer got an error: ' + err),
      complete: () => console.log('Observer got a complete notification', this.clusters),
    }

    this.predictions = this.bigqueryApi.getResults().subscribe(myObserver)
  }

  ngOnDestroy() {
    this.predictions.unsubscribe();
  }
}
