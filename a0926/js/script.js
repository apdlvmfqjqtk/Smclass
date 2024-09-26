// ajax이용한 데이터가져오기

//jquery 선언 시작
$(function () {
  let count = 1; //이 카운트값이 입력 데이터 넘버가 json 데이터의 총 length+1로 출력시키기 위한 전역 변수 설정
  let total = 0; //total과 avg는 변수값이 숫자 데이터로 저장되었으면 해서 아무 숫자나 집어넣어 숫자 데이터 변수로 전역 설정
  let avg = 0;
  let id_num; // 각각의 지역마다 var id_num을 지정하는건 귀찮으니 언제든지 id_num = ㅁㄴㅇㄹ 지정이 가능하도록 전역 변수 설정
  let tr_this;
  let temp = 0;
  //data 불러오기 시작
  // $("#dataBtn").click(function () {
  $(function () {
    // alert("데이터 불러오기 시작.")

    //ajax 선언 시작
    $.ajax({
      url: "js/stuData.json",
      type: "get",
      data: "",
      dataType: "json",
      //data불러오기 성공 이벤트 시작
      success: function (data) {
        console.log(data)
        let s_data = "";
        // alert("데이터 불러오기 성공.")
        for (var i = 0; i < data.length; i++) {
          count++;
          console.log("caount: " + count);
          let total = (data[i].kor + data[i].eng + data[i].math);
          let avg = (total / 3).toFixed(2);
          s_data += `<tr id='${data[i].no}'>`
          s_data += `<td>${data[i].no}</td>`
          s_data += `<td>${data[i].name}</td>`
          s_data += `<td>${data[i].kor}</td>`
          s_data += `<td>${data[i].eng}</td>`
          s_data += `<td>${data[i].math}</td>`
          s_data += `<td>${total}</td>`
          s_data += `<td>${avg}</td>`
          s_data += `<td> 
                     <button class="updateBtn">수정</button>
                     <button class="delBtn">삭제</button>
                     </td>`
          s_data += `</tr >`
        }
        $("#tbody").html(s_data)
      }, //data 불러오기 성공 이벤트 끝
      //data 불러오기 실패 이벤트 시작
      error: function (data) {
        alert("데이터 불러오기 실패.")
      } //data 불러오기 실패 이벤트 끝
    });//ajax 선언 끝
  });// data 불러오기 이벤트 끝

  //data 입력 이벤트 시작
  $(document).on("click", "#create", function () {
    alert("입력 시작.")

    //입력받은 데이터 변수 저장
    let name = $("#name").val();
    let kor = Number($("#kor").val());
    let eng = Number($("#eng").val());
    let math = Number($("#math").val());
    total = (kor + eng + math);
    avg = (total / 3).toFixed(2);

    //입력을 하였는지 확인하는 if문 / $(id)값의 글자 길이가 1보다 짧다면(0이라면) if문을 실행한다.
    if ($("#name").val().length < 1 || $("#kor").val().length < 1 || $("#eng").val().length < 1 || $("#math").val().length < 1) {
      alert("데이터를 입력하셔야 저장이 가능합니다.")
      return false;
    }

    alert("입력 중입니다...")

    //if문을 통과했을 시 데이터 tr에 입력 시작
    let s_data = "";
    // let count = 1;
    s_data += `<tr id='${count}'>`
    s_data += `<td>${count}</td>`
    s_data += `<td>${name}</td>`
    s_data += `<td>${kor}</td>`
    s_data += `<td>${eng}</td>`
    s_data += `<td>${math}</td>`
    s_data += `<td>${total}</td>`
    s_data += `<td>${avg}</td>`
    s_data += `<td> 
               <button class="updateBtn">수정</button>
               <button class="delBtn">삭제</button>
               </td>`
    s_data += `</tr >`

    alert("입력이 완료되었습니다");
    //입력한 데이터를 tbody에 추가시킴
    $("#tbody").prepend(s_data);

    //입력칸에 적어 둔 데이터 삭제
    $("#name").val("");
    $("#kor").val("");
    $("#eng").val("");
    $("#math").val("");

    count++;
  }); // 입력 버튼 이벤트 끝

  //삭제 버튼 이벤트 시작
  $(document).on("click", ".delBtn", function () { //삭제 버튼을 누른다면...
    //id_num이라는 변수는 현재 위치 (class="delBtn")의 가장 가까운 tr(closest("tr"))의 id속성값이야(attr()) )
    id_num = $(this).closest("tr").attr("id");
    console.log(id_num);
    if (confirm(id_num + "번 학생 성적을 삭제하시겠습니까?")) {
      $("#" + id_num).remove(); // $(#$(this).closest("tr").attr("id").remove
      alert(id_num + "번 학생 성적이 삭제되었습니다.");
    }
  }); // 삭제 버튼 이벤트 끝

  //수정 버튼 이벤트 시작 
  $(document).on("click", ".updateBtn", function () {
    //수정 버튼이 클릭이 되어 있는지 확인
    if (temp == 1) {
      alert("수정 완료 또는 수정 취소 버튼을 먼저 클릭하셔야 합니다.");
      return false;
    }
    $(this).css({ "color": "aqua", "font-weight": "600" })
    tr_this = $(this);

    alert("수정을 시작합니다");
    let m_data = $(this).closest("tr");
    console.log(m_data);
    console.log(m_data.children("td:eq(1)").text()); //m_data(tr)의 자식 중 ()번째 td요소 의 text값 출력
    console.log(m_data.children("td:eq(2)").text());

    $("#name").val(m_data.children("td:eq(1)").text())
    $("#kor").val(m_data.children("td:eq(2)").text())
    $("#eng").val(m_data.children("td:eq(3)").text())
    $("#math").val(m_data.children("td:eq(4)").text())

    //입력 버튼 삭제 & 수정완료, 수정취소 버튼 생성
    $("#create, #update, #updateCancel").toggle();
    temp = 1;
  }); //수정 버튼 이벤트 끝


  //수정 완료 이벤트 시작
  $(document).on("click", "#update", function () {
    //입력한 데이터를 변수에 기입
    tr_this.css({ "color": "black", "font-weight": "400" })
    let name = $("#name").val();
    let kor = Number($("#kor").val());
    let eng = Number($("#eng").val());
    let math = Number($("#math").val());
    total = kor + eng + math;
    avg = (total / 3).toFixed(2);

    //데이터를 입력하였는지 확인
    if( name == "" || kor == "" || eng == "" || math == "" ) {
      alert("데이터를 입력하셔야 저장이 가능합니다.")
      return false;
    }


    alert("수정이 완료되었습니다.");
    $("#create, #update, #updateCancel").toggle();
    temp = 0;
  }); //수정 완료 이벤트 끝


  //수정취소 버튼 이벤트 시작
  $(document).on("click", "#updateCancel", function () {
    tr_this.css({ "color": "black", "font-weight": "400" })
    alert("수정이 취소되었습니다.");
    //입력 버튼 생성 & 수정완료, 수정취소 버튼 삭제
    $("#create, #update, #updateCancel").toggle();

    //입력하고 있던 데이터 삭제
    $("#name").val("");
    $("#kor").val("");
    $("#eng").val("");
    $("#math").val("");

    temp = 0;
  }); //수정취소 버튼 이벤트 끝



}); //jquery 선언 끝