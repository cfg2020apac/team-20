import { Component, OnInit } from '@angular/core';
export interface PeriodicElement {
  name: string;
  position: number;
  weight: number;
  symbol: string;
}

// const ELEMENT_DATA: PeriodicElement[] = [
//   {position: 1, name: 'Hydrogen', weight: 1.0079, symbol: 'H'},
//   {position: 2, name: 'Helium', weight: 4.0026, symbol: 'He'},
//   {position: 3, name: 'Lithium', weight: 6.941, symbol: 'Li'},
//   {position: 4, name: 'Beryllium', weight: 9.0122, symbol: 'Be'},
//   {position: 5, name: 'Boron', weight: 10.811, symbol: 'B'},
//   {position: 6, name: 'Carbon', weight: 12.0107, symbol: 'C'},
//   {position: 7, name: 'Nitrogen', weight: 14.0067, symbol: 'N'},
//   {position: 8, name: 'Oxygen', weight: 15.9994, symbol: 'O'},
//   {position: 9, name: 'Fluorine', weight: 18.9984, symbol: 'F'},
//   {position: 10, name: 'Neon', weight: 20.1797, symbol: 'Ne'},
// ];
@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {
  // displayedColumns: string[] = ['position', 'name', 'weight', 'symbol'];
  displayedColumns: string[] = ['Opportunity', 'Organization', 'Date', 'Hours','Action/Status'];

   dataSource ;
  constructor() { }
  ELEMENT_DATA;
  ngOnInit(): void {
    this.ELEMENT_DATA= [
      {position: 1, name: 'AB', weight: 12333, symbol: 'H'},
      {position: 2, name: 'C', weight: 4.0026, symbol: 'e'},
      {position: 3, name: 'D', weight: 6.941, symbol: 'i'},
      {position: 4, name: 'D', weight: 9.0122, symbol: 'B'},
      {position: 5, name: 'B', weight: 10.811, symbol: 'B'},
      {position: 6, name: 'D', weight: 12.0107, symbol: 'C'},
      {position: 7, name: 'N', weight: 14.0067, symbol: 'A'},
      {position: 8, name: 'R', weight: 15.9994, symbol: 'O'},
      {position: 9, name: 'G', weight: 18.9984, symbol: 'F'},
      {position: 10, name: 'H', weight: 20.1797, symbol: 'N'},
    ];
    this.dataSource = this.ELEMENT_DATA;

  }

}
