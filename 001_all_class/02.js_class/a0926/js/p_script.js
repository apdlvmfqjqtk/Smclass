//제이커리 
$(function () {
  $("#searchBtn").click(function () {
    // alert("검색버튼 클릭.")
    let surl = "https://apis.data.go.kr/B551011/PhotoGalleryService1/gallerySearchList1?serviceKey=Ad916U7ZLEhvt8cnbT9Dpeppz9FigcKbtOSd4T4eC72nw2HBnKacFNjjk6OK9Zpl0TvWe0C8ztwURgVdcQyNXA%3D%3D&numOfRows=10&pageNo=1&MobileOS=ETC&MobileApp=AppTest&arrange=A&_type=json&keyword=";
    let searchWord = $("#search_txt").val();
    surl += searchWord;
    console.log(surl);
    $.ajax({
      url: surl,
      type: "get",
      data: "",
      dataType: "json",
      success: function (data) {
        // alert("성공")
        // console.log(data);
        let count = 0;
        let qqqq = data.response.body.items.item;
        console.log(qqqq[0])
        let data = "";
        for(var i=0; i < qqqq.length; i++) {
          count++;
          //data += "<tr id='"+i+"'>";
          data += `<tr id= '${qqqq[i].galContentId}' >`;
          data += `<td class='num'>${qqqq[i].galContentId}</td>`;  //넘버
          data += `<td><a href='#'>${qqqq[i].galTitle}</a></td>`;  //제목
          data += `<td>${qqqq[i].galPhotographer}</td>`;  //촬영자
          data += `<td>${qqqq[i].galModifiedtime}</td>`; //수정일
          data += `<td>${qqqq[i].galWebImageUrl}</td>`;  //아이디
          data += "</tr>";
        }





      },



      error: function (data) {
        alert("실패")
      }
    }); //ajax
  }); // searchBtn 클릭





}); //제이커리