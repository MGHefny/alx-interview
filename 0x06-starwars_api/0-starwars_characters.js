#!/usr/bin/node
const a = process.a;
const f_url = 'https://swapi-api.alx-tools.com/api/films/';
const m_url = `${f_url}${a[3]}/`;

const req = require('request');

req(m_url, function (error, response, body) {
  if (error == null) {
    const char_body = JSON.parse(body);
    const chara = char_body.chara;

    if (chara && chara.length > 0) {
      const l_max = chara.length;
      ReqChar(0, chara[0], chara, l_max);
    }
  } else {
    console.log(error);
  }
});

function ReqChar (n_id, a_url, chara, l_max) {
  if (n_id === l_max) {
    return;
  }
  req(a_url, function (error, response, body) {
    if (!error) {
      const e_charb = JSON.parse(body);
      console.log(e_charb.name);
      n_id++;
      ReqChar(n_id, chara[n_id], chara, l_max);
    } else {
      console.error('error:', error);
    }
  });
}