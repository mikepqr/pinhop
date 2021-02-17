# https://pinboard.in/stylesheets/main.css
css = """
body
{
  color:#333;
  margin-left:20px;
  font-size:13px;
  font-family: helvetica, sans-serif;
  word-wrap:break-word;
  text-align:center;
}



blockquote
{
    margin-left:20px;
    margin-bottom:0px;
    color:#247;
}

#content
{
    width:1050px;
    margin-left:auto;
    margin-right:auto

}

/* basic elements */
td { font-size:13px; }
p  { margin-top:2px;margin-bottom:12px }
li { margin-bottom:10px }


/* global link styling */
a
{
    text-decoration:none;
    color:#11a;
}
a:visited { color:#51a }
a.edit { font-size:1em; }

h1
{
    font-size:2em;
    font-family:helvetica;
    font-weight:normal;
    margin-top:10px;
}
h2 {
    font-size:1.3em;
    font-family:helvetica;
    font-weight:normal;
}
h3 { font-size:110%;background:#eaefff;}
h4 { font-size:100%;background:#dfc;}

code
{
  margin-left:20px;
  color:#22a;
  font-family:monaco;
}


/* BOOKMARK STYLING */
a.fetch_err
{
    font-size:80%;
    color:red;
    font-weight:bold;
}
.cached
{
    color:#aaa;
    font-size:1.2em;
}
.cached:visited {color:#aaa}
.description
 {
    line-height:120%;
    margin-top:2px;
    color:#555;
}
.star
{
  color:#ccc;
  margin-left:-20px;
  font-size:1.3em;
  cursor:pointer;
  float:left;
}
.selected_star { color:#22a; }
.confirm
{
    color:red;
    visibility:hidden;
    display:none;
}
.delete_link { display:inline; }
.when {  font-size:90%;color:#777 }
a.url_display:hover { color:#44d; }

a.source { color:#77c;}
a.tag {color:#a51;line-height:190%;}
a.bundle { color:#b40;font-weight:bold }
a.bundle { color:#a21;font-weight:bold }

#bundle_names a
{
    line-height:180%;
}

#bundle_names
{
    margin-top:20px;
}

a.delete { color:#aaa }
a.delete:visited { color:#aaa }
a.delete:hover { color:#44d; }

a.edit { color: #aaa }
a.edit:hover { color:#44d; }
a.edit:visited { color:#ccc }

a.destroy { color:red; }
a.destroy:visited { color:red; }

a.copy_link { color: #bbb }
a.copy_link:hover { color:#44d; }
.copy_confirm { color:#aaa; }
.faint {color:#aaa}

.edit_links
{
    display:inline;
}




.url_link
{
    font-size:90%;color:#888;
}
.bookmark
{
  margin-bottom:1.3em;
  padding:3px;
  width:600px;
  margin-left:0px;
  border:0px solid red;
  float:left;
 }
.bookmark_title { line-height:130%;font-size:110%; }
a.url_display
{
    color:#888;
    font-size:0.9em;
}
.private a { padding:1px;border:0px;}
.private { background:#ddd;border:1px solid #d1d1d1; }
.unread { color:#b41 }
a.unread { color:#b41 }
a.has_bmark { color:#aaa }

/* BOOKMARK LISTS */
a.list { color:#163; }
.lists { color:#163; }

/* ?? */
.flash { color:green;background:#efe }

/* MAIN BANNER AND NAV */
#banner
{
  background:white;
  color:black;
  border-bottom:1px dotted #aaa;
  margin-bottom:0.7em;
  width:980px;
  padding-bottom:9px;
  text-align:left;
}


#banner a { color:#aaa; }
#banner a.admin { color:#e00 }
#banner a.banner_username { color:blue; }
#pinboard_name { font-size:18px; }


#logo { float:left;width:325px;color:#aaa;}
.pin_logo { margin-right:2px; }
#top_menu
{
    margin-top:2px;
    float:right;
}
#top_menu a { color:blue }


/* user alert */
.alert
{
    color:#333;
    background:#ced;
    padding:10px;
    width:550px;
    border:1px solid #acc;
}


#login_box
{
  float:right;
}


/* BASIC PAGE STRUCTURE */
#main_column
{
    width:700px;
    min-height:700px;
    text-align:left;
    float:left;
    position:relative;
    #border:1px solid #fa8;

}

#right_bar
{
    float:left;
    margin-left:10px;
    text-align:left;
    width:330px;
    #border:1px solid #cfd;
}


.rss_linkbox
{
    float:right;
    margin-right:30px;
}

a.rss_link
{
    color:#ee9922;
    font-size:0.8em;
}

.bookmark_count_box
{
    float:left;
    width:36px;
    padding-right:1.1em;
}


/* USER HOME PAGE */
.user_navbar
{
    margin-bottom:0.7em;
}

.subscribe_link
{
    margin-left:30px;
    float:left;
    margin-right:8px;
    color:#aac;
}

.unsubscribe_link
{
    margin-left:30px;float:left;
    color:#caa;
}

.source_filter
{
    background:#ddf;
    color:#555;
}

.edit_checkbox
{
  display:none;
  float:left;
  margin-left:-40px;
  width:40px;
}

.tag_table
{
    float:left;
    margin-right:10px;
}


/* howto page */
a.bookmarklet
{
    background:#ffe;
    border:1px dotted #aaa;
    color:#444;
    padding:1px 2px 0px 2px;
    font-size:90%;
}
.heading { color:#555;}
.homepage_heading {
    margin-top:25px;
    margin-bottom:5px;
    color:#338;
    font-size:1em;
}


.error { color:red }

a.systag { color:#c41 }
a.next_prev { color:#777 }

#bottom_next_prev { float:left; }


 #star_operations
 {
  border:0px solid blue;width:300px;float:left;
 }


.selected_star
{
  color:#559;
}



.display { float:left }
.unimplemented { color:#aaa }


/* bulk and single edit form */
#bulk_links p { line-height:0.7em; }

#edit_bookmark_form
{
  border: 0px solid #aaa;
  background:#fff;
  width:500px;
  padding:4px;
  padding-left:10px;
  float:left;
  color:#888;
  display:none;
  visibility:hidden;
}

#edit_bookmark_form p
{
  line-height:100%;
  margin-bottom:0px;
  color:#888;
}

#edit_bookmark_form input
{
  font-size:90%;
  border:1px solid #ddd;
  margin-bottom:3px;
}

#edit_bookmark_form textarea
{
  font-size:90%;
  border:1px solid #ddd;
  margin-bottom:3px;
}

.edit_form_input
{
    width:490px;
    margin-top:10px;
    font-size:12px;
    background:#fff;
    padding-top:3px;
}
#edit_form_checkboxes
{
    margin-top:10px;
    margin-bottom:10px;
}
#edit_form_suggested_tags
{
    margin-top:10px;
    margin-bottom:18px;
}


#tag_cloud
{
  float:left;
  width:350px;
  text-align:justify;
  line-height:110%;
  margin-top:20px;
}

.bookmark_count {
  font-size:80%;
  color:#aaa;
 }

 .tag_count {  font-size:90%;color: #aaa; }


#years
{
    border:1px solid orange;
    float:left;
}
#years a
{
    color:#aaa;
    font-size:8pt;

}

#bulk_links
{
  margin-bottom:20px;
}
 a.mark_read { color:#a81}



#active_users
{
  float:left;
  margin-left:40px;
}

#related_tags
{
  width:250px;border:0px solid red;
  }

#timer
{
  color:#bbb;float:right;font-size:10px;font-family:helvetica;margin-top:4px;
}

#footer
{
  margin-top:3em;color:#888;
 }

a.help
{
  color:#2a2;background:#ffc}


.tabs { background:#fff;padding:0px;margin-bottom:0px; }
.tab_select
{
  float:left;
  margin-right:10px;
}


a.filter { color:#999}


.disabled { color:#888;background:#ccc}

.upgrade_header {
    font-size:1.4em;color:#666;
    font-weight:bold;margin-top:30px;
    margin-bottom:10px;background:#fff}





a.twitter_user { color:#000099; }
#em { font-weight:bold;color:#555;font-style:normal}



.tweet_date { color:#aaa;font-size:90%;}
.twitter_name { font-weight:bold; }
a.twitter_account { color:#66c}
a.outside_resource { color:blue;text-decoration:underline; }


a.selected {color:blue}

.selected { background:#fafafa; }

/* pagination and sort order links */
#per_page_picker {color:#888;float:left;margin-left:90px;text-align:center; }
#per_page_picker a {color:#aaa; }
#per_page_picker a.per_page_selected { background:#ff8;color:blue; }

.pagination_select
{
    display:inline;
   /* margin-right:30px; */
}
#sort_order_picker { display:inline; }
#sort_order_picker a.sort_order_selected { color:#888;}
#sort_order_picker a { color:#ccc; }
#sort_order_picker { color:#aaa; }
.sort_arrow { font-size:15px;font-family:monaco }
@-moz-document url-prefix() {
   .sort_arrow { font-size:20px;}
}


#tag_cloud a.tag_heading_selected { font-weight:bold;color:#333 }
#tag_cloud table{ line-height:100%;}
#tag_cloud_header a { color:#aaa; }

ul.clean { list-style-type:none;padding-left:0px;}

.small_username
{
    float:left;
    padding-right:1em;
}


.twitter_account_title /* used on settings page */
{
    font-size:1.3em;color:#59d
}

a.twitter_account_title /* used on settings page */
{
    color:#59d
}

/* tabs stuff */
.help_box
{
    line-height:120%;
    background:#ffe;
    padding:10px;
    border:1px solid #dba;
}

.window_title
{
    font-weight:bold;
    font-size:1.2em;
    color:#555;
    margin:0px;
    margin-top:20px;
    padding:0px;
    cursor:pointer;
}
/* tour page */
h1.tour_heading
{
    font-size:2em;
    font-family:helvetica;
    font-weight:normal;
    margin-top:10px;
}
h2.tour_heading
{
    font-size:1.5em;
    font-family:helvetica;
    font-weight:normal;
    background:#fff;
    margin-top:37px;
    margin-bottom:20px;
}


/* SETTINGS PAGE */
h2.settings_heading
{
    font-size:1.3em;
    font-family:helvetica;
    font-weight:normal;
    background:#fff;
    margin-top:7px;
    margin-bottom:15px;
}

.email_secret
{
    color:#05a;
    font-weight:bold;
}

#import_history_table
{
    float:left;
    padding:5px;
    border:1px solid #ccc;
}

.tab {
  float:left;
  text-align:center;
  padding-bottom:0.2em;
  width:100px;
  height:15px;
   border-top:1px solid #ffc;
   border-bottom:1px solid #aaa;
}

.tab_spacer
{
    float:left;
    height:15px;
    padding-bottom:0.2em;
    width:98px;
    border-top:1px solid  #fff;
    border-bottom:1px solid #aaa;
    color:#ffc;
}

.tab_selected {
    border:1px solid #aaa;
    border-bottom:1px solid #eee ;
    background:#eee }
#tab_panes
{
  border:1px solid #aaa;
  border-top:0px solid #fff;
  padding:2em;
  margin:0px;
}


/* UPGRADE PAGE */
#upgrade_left_column
{
    width:400px;
    float:left;
}

#upgrade_right_column
{
    margin-left:40px;
    width:250px;
    float:left;
}
.account_status_box
{
    padding:10px;border:1px solid #abd;
}

/* USER ACCOUNT PAGE */
#profile_main_column
{
    width:1200px;
    float:left;
    text-align:left;
}

#profile_left_column
{
    width:350px;
    float:left;
}

#profile_right_column
{
    float:left;
    margin-left:40px;
    width:450px;
}

#profile_admin_column
{
    float:left;
    width:300px;
    font-size:11px;
    text-align:left;
    padding:5px;
    height:800px;
    background:#efe
}

.service_box
{
    float:left;
    width:350px;
    margin-bottom:20px;
}

#name_string
{
    font-size:140%
}

#archival_column
{
    float:left;
    width:300px;
}


a.upgrade_link
{
    text-decoration:underline;
    font-weight:bold;
}





/* signup */
.signup_button
{
    text-align:center;
    font-size:1.2em;
    font-weight:bold;
    color:#444;
    background:#dfa;
    border:1px solid #888;
    border-radius:15px;
    -moz-box-shadow: 1px 1px 1px #555;
    -webkit-box-shadow: 1px 1px 1px #888;
    box-shadow: 1px 1px 2px #888;
    padding-left:0px;
    padding-top:5px;
    padding-bottom:2px;
    width:230px;
    height:20px;
    margin-left:30px;
    margin-top:50px;
}


/* NOTES */
#note_tagbox
{
    margin-bottom:15px;
    width:500px;
    padding:4px;
    background:#ffc;
    border:1px dotted orange;
}
#note_right_column
{
    text-align:left;
    width:250px;
    float:left;
}
blockquote.note
{
    margin-left:0px;
    width:490px;
    line-height:130%;
    font-family:verdana
}
.note_last_updated
{
    color:#ca4;
    font-size:0.9em
}

.notes_pagination
{
    margin-bottom:20px;
    margin-top:10px;
}


/* PUBLIC PROFILE */
input.profile_input
{
    width:350px;
}
textarea.profile_input
{
    width:350px;
    height:140px;
}

#public_edit_right_column
{
    margin-top:20px;
    text-align:left;
}

.public_name_value
{
    font-size:18pt;
    color:#555;
}

#public_profile_left_column
{
    float:left;
    text-align:left;
    min-height:700px;
    width:380px;
    margin-right:20px;
}
#public_profile_left_column h2
{
    margin-top:10px;
}
#public_profile_left_column a.username
{
    color:blue;
}
#public_profile_subscribe_div
{
    margin-bottom:10px;
    color:#888;
}
#public_profile_attributes td
{
    vertical-align:top;
}
#public_profile_tag_cloud
{
    float:left;
    width:300px;
    text-align:left;
}

#public_profile_searchbox
{
    margin-left:30px;
    margin-top:10px;
    text-align:left;
    float:left;
}

/* SEARCH PAGE */
#search_right_bar
{
    float:left;
    margin-left:10px;
    text-align:left;
    width:300px;
}
.search_button
{
    margin-top:10px;
}

#tweet_searchbox
{
    margin-top:20px;
    float:left;
    margin-left:10px;
}

/* stuff for import/export instructions */
.pprofile_heading
{
    color:#888;
}

ol.howto { list-style-type:decimal;margin-top:10px; margin-bottom:20px;}
li.howto { list-style-type:decimal;margin-top:20px; }
tt { background:#ffa;font-family:verdana;color:#37d; }
li.import_instructons
{
    line-height:150%;
}
ol.download_instructions
{
    margin-top:10px;
}

/* ADMIN STUFF */
#searchbox fieldset
{
    opacity:0.5;
    border:1px solid #ff4444;
    background:#ffccbb;
}


/* bulk edit box */
#bulk_edit_options
{
    display:none;
    margin-top:9px;
    width:650px;
}

 #bulk_edit_box
 {
    display:block;
    color:#777;
    border:1px solid #aaa;
    background:#eee;
    padding:0px;
    margin:0px;
 }

 #confirm
 {
    display:none;
    background:#35a;
    padding:3px;
    color:white;width:650px;

}
 #bulk_top_bar
 {
    background:#ddd;
    height:20px;
    padding:3px 10px 0px 10px;
    border-bottom:1px solid #ccc
}
"""
