// const express = require('express')
const axios = require('axios');

var postData = {
            "kodepemda": 3202,
            "tahunmulai": 2016,
            "tahunselesai": 2021,
            "periode_rpjmd": 2016-2021
  };
  
  let axiosConfig = {
    headers: {
        'Content-Type': 'application/json',
        "Access-Control-Allow-Origin": "*",
        "authorization" : "Bearer [d86377214cdd20db6ce9ab67c92a428v]"
    }
  };
  
  axios.post('https://sipd.go.id/run/serv/push_rpjmd.php?tahun_anngaran=20162021&kodepemda=3202', postData, axiosConfig)
  .then((res) => {
    console.log("RESPONSE RECEIVED: ", res);
  })
  .catch((err) => {
    console.log("AXIOS ERROR: ", err);
  })