# -*- coding: UTF-8 -*-
import csv
import json
import sys
import requests
import time

reload(sys)
sys.setdefaultencoding('utf-8')


base_url="https://www.zhihu.com/api/v4/infinity/hot_responders?limit=20&offset="
user_agent="""Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36x-ab-param: se_v_v005=0;tp_club_entrance=1;li_car_meta=1;qap_labeltype=1;se_searchvideo=3;se_v_drop=0;soc_feed_intelligent=3;ge_ge01=5;se_v046=0;zr_test_aa1=1;se_hi_trunc=0;tsp_ioscard2=0;pf_noti_entry_num=1;pf_adjust=1;li_vip_verti_search=0;ls_videoad=2;ls_video_commercial=0;zr_slot_training=2;tp_zrec=1;tp_club_feed=0;tsp_ios_cardredesign=0;pf_creator_card=1;li_svip_cardshow=1;se_click_v_v=1;se_major=0;tp_club_bt=0;tp_m_intro_re_topic=1;li_ebook_gen_search=2;se_college=default;zr_search_sim2=2;top_root=0;li_viptab_name=0;zr_km_answer=open_cvr;tp_topic_tab_new=0-0-0;pf_foltopic_usernum=0;ls_recommend_test=4;ge_ge02=6;se_auth_src=0;ug_newtag=1;zr_search_paid=1;li_answer_card=0;tp_club_top=0;tp_club_qa_entrance=1;tp_meta_card=0;li_paid_answer_exp=0;se_usercard=0;se_aa_base=0;se_colorfultab=1;se_guess=0;tp_dingyue_video=1;zr_ans_rec=gbrank;zr_topic_rpc=0;zr_art_rec=base;se_merge=0;top_quality=0;se_v_bert2=1;zw_sameq_sorce=995;pf_fuceng=1;ls_fmp4=0;zr_search_topic=1;se_wil_act=0;se_videobox=1;tp_fenqu_wei=1;pf_newguide_vertical=0;li_yxzl_new_style_a=1;zr_training_first=false;se_preset=0;zr_rel_search=base;se_bert128=0;tp_topic_tab=0;zr_training_boost=true;zr_expslotpaid=1;se_searchwiki=0;tsp_adcard2=0;se_major_v2=0;se_sug_term=0;tp_contents=2;zr_sim3=0;se_v_v006=0;se_whitelist=1;top_v_album=1;li_svip_tab_search=1;se_return_1=0;ug_follow_topic_1=2;se_zp_boost=0;se_recommend=0;top_ebook=0;tp_club__entrance2=1;tp_discover=1;qap_question_author=0;se_topicfeed=0;se_club_ui=0;se_col_boost=1;se_t2sug=0;se_mobilecard=0;tp_clubhyb=0;tsp_hotlist_ui=3;qap_question_visitor= 0;pf_profile2_tab=0;li_topics_search=0;li_catalog_card=1;top_test_4_liguangyi=1;li_edu_page=old;li_panswer_topic=0;zr_slotpaidexp=8;tp_club_fdv4=0;tp_header_style=1;soc_notification=1;top_universalebook=1;tsp_ad_cardredesign=0;li_video_section=1;li_yxxq_aut=A1;zr_intervene=0;zr_rec_answer_cp=open;se_adsrank=4;se_ffzx_jushen1=0;se_v_rate=17;tp_sft=a;tp_topic_style=0;se_entity22=1"""

headers={
    'cookie':'_zap=d6371a96-21ab-4a21-8140-3186e29062bc; d_c0="ACAbQfd-FhGPTi7VJoFoH3zPfVFmRXl6jSs=|1586347454"; _ga=GA1.2.1680444676.1586347457; z_c0=Mi4xMnFSLUFBQUFBQUFBSUJ0QjkzNFdFUmNBQUFCaEFsVk5DZlI3WHdBRXU2dzNHOFdpcXFDZE1SNTl0RFdTd3dBR1JR|1586406921|3a19d464cbe5942fb8242725cac5f445e522e015; _xsrf=YG2QLZc615fKSVu8Hr0KrfKnCvtisv1B; __utmc=51854390; __utmv=51854390.100-1|2=registration_date=20140923=1^3=entry_date=20140923=1; _gid=GA1.2.1582238188.1594519496; q_c1=57b760e0b6ed47cd909f4b27ff22afa2|1594555791000|1586768293000; __utmz=51854390.1595046494.3.3.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; SESSIONID=YoEfZrV3eSodvy4p4C5FB5cSRgBoVUcMvcQDdnwI57j; JOID=UVkRA0zpTxPedU5OMOqJyMgd8QgmsiVSvys-HQeIHnm-BDN4RceIAoJzSU8z19M_1YH-gNgp0YTnS1XyqI_UaQw=; osd=UVgTAU7pThHcd05PMuiLyMkf8womsydQvSs_HwWKHni8BjF4RMWKAIJyS00x19I914P-gdor04TmSVfwqI7Waw4=; tst=r; oauth_from="/settings/account"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1595329030,1595335101,1595342040,1595343475; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1595405971; __utma=51854390.1680444676.1586347457.1595046494.1595406197.5; __utmb=51854390.0.10.1595406197; KLBRSID=e42bab774ac0012482937540873c03cf|1595406366|1595381553',
    'user-agent':user_agent
}

writer = csv.writer(open("consultData.csv","wb+"))
writer.writerow(["答主","评分","咨询次数","咨询单价","总金额","描述",'详情'])

def requestOnece(url):

    req=requests.get(url,headers=headers)

    data = json.loads(req.text)

    for row in data['data']:
        writer.writerow([
            row['fullname'],
            row['score'],
            row['conversation_count'],
            row['question_price'],
            row['question_price']*row['conversation_count'],
            row['description'],
            "www.zhihu.com/consult/people/"+row["id"]
        ])


for offset in range(0,101,20):
    print offset
    url=base_url+str(offset)
    requestOnece(url)
    time.sleep(5)