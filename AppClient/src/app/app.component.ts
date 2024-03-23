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

  constructor(private formBuilder: FormBuilder,
              private appService: AppService) {
    this.form = this.formBuilder.group({
      tokens: [],
      isPrd: [false]
    });
  }

  onSend() {
    debugger;
    const tokensStr = this.form.controls['tokens'].value as string;
    const tokensArray = tokensStr.split(',').map(token => token.trim()).filter(Boolean);
    console.log(tokensArray)
    // this.appService.postData(tokensArray).subscribe(response => {
    //   console.log('Response from server:', response);
    // }, error => {
    //   console.error('Error:', error);
    // })
  }

}
