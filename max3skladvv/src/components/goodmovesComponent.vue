<template>
<div>

<button type="button"
class="btn btn-primary m-2 fload-end"
data-bs-toggle="modal"
data-bs-target="#exampleModal"
@click="addClick()">
 Добавить перемещение товара
</button>

<table class="table table-striped">
<thead>
    <tr>
        <th>
            Наименование склада откуда
        </th>
        <th>
            Наименование склада куда
        </th>
        <th>
            Наименование товара
        </th>
        <th>
            Кол-во
        </th>
        <th>
            Дата и время
        </th>
    </tr>
</thead>
<tbody>
    <tr v-for="acc in goodmoves" v-bind:key="acc.id">
        <td>{{acc.nameStockFrom}}</td>
        <td>{{acc.nameStockTowhere}}</td>        
        <td>{{acc.nameGood}}</td>
        <td>{{acc.qty}}</td>
        <td>{{acc.datetime}}</td>       
        <td>
            <button type="button"
            class="btn btn-light mr-1"
            data-bs-toggle="modal"
            data-bs-target="#exampleModal"
            @click="editClick(acc)">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
                <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
                <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
                </svg>
            </button>
            <button type="button" @click="deleteClick(acc.id)"
            class="btn btn-light mr-1">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash-fill" viewBox="0 0 16 16">
                <path d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z"/>
                </svg>
            </button>

        </td>
    </tr>
</tbody>

</table>

<div class="modal fade" id="exampleModal" tabindex="-1"
    aria-labelledby="exampleModalLabel" aria-hidden="true">
<div class="modal-dialog modal-lg modal-dialog-centered">
<div class="modal-content">
    <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">{{modalTitle}}</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal"
        aria-label="Close"></button>
    </div>

    <div class="modal-body">

            <div class="input-group mb-3">
                <span class="input-group-text">Склад откуда</span>
                <select class="form-select" v-model="nameStockFrom">
                    <option v-for="st in stocks" v-bind:key="st.id">
                    {{st.nameStock}}
                    </option>
                </select>
            </div>
            <div class="input-group mb-3">
                <span class="input-group-text">Склад куда</span>
                <select class="form-select" v-model="nameStockTowhere">
                    <option v-for="st in stocks" v-bind:key="st.id">
                    {{st.nameStock}}
                    </option>
                </select>
            </div>            

            <div class="input-group mb-3">
                <span class="input-group-text">Наименование товара</span>
                <select class="form-select" v-model="nameGood">
                    <option v-for="st in goods" v-bind:value="st.nameGood" v-bind:key="st.id">
                    {{st.nameGood}}
                    </option>
                </select>
            </div>        

        <div class="input-group mb-3">
            <span class="input-group-text">Количество</span>
            <input type="number" class="form-control" v-model="qty">
        </div>

        <div class="input-group mb-3">
            <span class="input-group-text">Дата</span>
            <input type="date" class="form-control" v-model="dateInp">
        </div>

        <div class="input-group mb-3">
            <span class="input-group-text">Время</span>
            <input type="time" class="form-control" v-model="timeInp">
        </div>

        <button type="button" @click="createClick()"
        v-if="id==0" class="btn btn-primary">
        Создать
        </button>
        <button type="button" @click="updateClick()"
        v-if="id!=0" class="btn btn-primary">
        Обновить
        </button>


    </div>

</div>
</div>
</div>


</div>
</template>

<script>
  import axios from "axios";
  
  export default {
    name: 'goodmovesComponent',
    data(){
    return{
        goodmoves:[],
        goods:[],
        stocks:[],
        modalTitle:"",
        id:0,
        nameStockFrom:"",
        nameStockTowhere:"",
        nameGood:"",
        qty:0,
        datetime:"yyyy-MM-dd HH:mm:ss",
//        API_URL:"https://localhost:7141/api/",
//        API_URL:"http://127.0.0.1:8000/",
//        API_URL:"https://mzakiryanovgmailcom.pythonanywhere.com/",
//API_URL : import.meta.env.VITE_API_URL || "https://mzakiryanovgmailcom.pythonanywhere.com/",
API_URL : import.meta.env.VITE_API_URL || "https://sklad-backend-docker.onrender.com/",
//API_URL :import.meta.env.VITE_API_URL || "https://unpackaged-pentamerous-kristyn.ngrok-free.dev/",
//        API_URL:"https://webapistockkz.azurewebsites.net/api/",
        dateInp:"",
        timeInp:"",
    }
},
methods:{


    refreshData(){
        axios.get(this.API_URL+"goodmoves")
        .then((response)=>{
            this.goodmoves=response.data;
        });
        axios.get(this.API_URL+"stocks")
        .then((response)=>{
            this.stocks=response.data;
        });
        axios.get(this.API_URL+"goods")
        .then((response)=>{
            this.goods=response.data;
        });        
    },
    addClick(){
        var current = new Date();
        var month = current.getMonth() + 1;
        var date = current.getDate();
        var hour = current.getHours();        
        var minute = current.getMinutes();
        var second = current.getSeconds();
        month = month > 9 ? month : "0"+month;
        date = date > 9 ? date : "0"+date;
        hour = hour > 9 ? hour : "0"+hour;
        minute = minute > 9 ? minute : "0"+minute;
        second = second > 9 ? second : "0"+second; 
        this.dateInp=current.getFullYear()+'-'+month+'-'+date;
        this.timeInp=hour + ":" + minute + ":" + second;       
        this.modalTitle="Добавить перемещение товара";
        this.id=0;
        this.nameStockFrom="";
        this.nameStockTowhere="";
        this.nameGood="";
        this.qty=0;
        this.datetime="yyyy-MM-dd HH:mm:ss"
    },
    editClick(acc){
        this.dateInp=acc.datetime.substring(0,10);
        this.timeInp=acc.datetime.substring(11,16);        
        this.modalTitle="Редактировать перемещение товара";
        this.id=acc.id;
        this.nameStockFrom=acc.nameStockFrom;
        this.nameStockTowhere=acc.nameStockTowhere;
        this.nameGood=acc.nameGood;
        this.qty=acc.qty;
        this.datetime=acc.datetime
    },
    createClick(){
        this.datetime=this.dateInp+'T'+this.timeInp+'Z';
        axios.post(this.API_URL+"goodmoves",{
            nameStockFrom:this.nameStockFrom,
            nameStockTowhere:this.nameStockTowhere,
            nameGood:this.nameGood,
            qty:this.qty,
            datetime:this.datetime,
        })
        .then((response)=>{
            this.refreshData();
//            alert(response.data);
        });
    },
    updateClick(){
        this.datetime=this.dateInp+'T'+this.timeInp+'Z';
        axios.put(this.API_URL+"goodmoves",{
            nameStockFrom:this.nameStockFrom,
            nameStockTowhere:this.nameStockTowhere,
            nameGood:this.nameGood,
            qty:this.qty,
            datetime:this.datetime,
            id:this.id,
        })
        .then((response)=>{
            this.refreshData();
//            alert(response.data);
        });
    },
    deleteClick(id){
        if(!confirm("Вы уверены, что хотите удалить запись?")){
            return;
        }

        axios.delete(this.API_URL+"goodmoves/"+id)
        .then((response)=>{
            this.refreshData();
 //           alert(response.data);
        });

    },
    FilterFn(){
        var id_goodFilter=this.id_goodFilter;
        var nameGoodFilter=this.nameGoodFilter;

        this.goodmoves=this.goodmovesWithoutFilter.filter(
            function(el){
                return el.id_good.toString().toLowerCase().includes(
                    id_goodFilter.toString().trim().toLowerCase()
                )&&
                el.nameGood.toString().toLowerCase().includes(
                    nameGoodFilter.toString().trim().toLowerCase()
                )
            });
    },
    sortResult(prop,asc){
        this.goodmoves=this.goodmovesWithoutFilter.sort(function(a,b){
            if(asc){
                return (a[prop]>b[prop])?1:((a[prop]<b[prop])?-1:0);
            }
            else{
                return (b[prop]>a[prop])?1:((b[prop]<a[prop])?-1:0);
            }
        })
    }

},
mounted:function(){
    this.refreshData();
}   
  }
</script>