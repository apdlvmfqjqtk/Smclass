//제이쿼리 선언
$(function () {
  //검색버튼 클릭 이벤트
$("#searchBtn").click(function () {
alert("버튼 클릭");
let surl = "https://apis.data.go.kr/B551011/PhotoGalleryService1/gallerySearchList1?serviceKey=918RE13GA7OY7ZEmUzApgbOeAcQoZ%2FaHsXWcqPAKQ9YNNPj83KOstRMRIUrCFIAcm9qj2R6b7NFZjp%2FYsYzJLg%3D%3D&numOfRows=10&pageNo=1&MobileOS=ETC&MobileApp=AppTest&arrange=A&_type=json&keyword=";
let searchWord = $("#search_txt").val();
surl += searchWord;
//ajax 선언
$.ajax ({
  url: surl,
  type: "get",
  data: "",
  dataType:"json",
  success:function(data) {
    alert("데이터 수신 성공");
    console.log(data) // 수신받은 데이터 콘솔창으로 확인
    let datalist = data.response.body.items.item; //내가 사용하려는 데이터의 위치점을 변수로 지정함으로 텍스트 수 줄임 
    var adata = "";
    for(var i=0; i< 10; i++) {
      adata += `<tr id='${datalist[i].galContentId}'>`;
      adata += `<td class='num'>${datalist[i].galContentId}</td>`;
      adata += `<td>${datalist[i].galTitle}</td>`;
      adata += `<td>${datalist[i].galPhotographer}</td>`;
      adata += `<td>${datalist[i].galModifiedtime}</td>`;
      adata += `<td><img src ="${datalist[i].galWebImageUrl}"></td>`;
      adata += "</tr>"
    } //데이터 불러와서 for문에 변수저장

    document.getElementById("tbody").innerHTML = adata;

  },
  error:function() { //데이터 수신에 실패했을 시 실행
    alert("실패");
  }



}); //ajax 선언 끝
}); // 검색버튼 클릭 이벤트 끝




}) //제이쿼리 선언 end