<?php
define('API_KEY','6629869721:AAEMcRi2MA4Ti-TNmoptXL9TXYzDW7-T9kM');
function makereq($method,$datas=[]){
    $url = "https://api.telegram.org/bot".API_KEY."/".$method;
    $ch = curl_init();
    curl_setopt($ch,CURLOPT_URL,$url);
    curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);
    curl_setopt($ch,CURLOPT_POSTFIELDS,http_build_query($datas));
    $res = curl_exec($ch);
    if(curl_error($ch)){
        var_dump(curl_error($ch));
    }else{
        return json_decode($res);
    }
}
function apiRequest($method, $parameters) {
  if (!is_string($method)) {
    error_log("Method name must be a string\n");
    return false;
  }
  if (!$parameters) {
    $parameters = array();
  } else if (!is_array($parameters)) {
    error_log("Parameters must be an array\n");
    return false;
  }
  foreach ($parameters as $key => &$val) {
    // encoding to JSON array parameters, for example reply_markup
    if (!is_numeric($val) && !is_string($val)) {
      $val = json_encode($val);
    }
  }
  $url = "https://api.telegram.org/bot".API_KEY."/".$method.'?'.http_build_query($parameters);
  $handle = curl_init($url);
  curl_setopt($handle, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($handle, CURLOPT_CONNECTTIMEOUT, 5);
  curl_setopt($handle, CURLOPT_TIMEOUT, 60);
  return exec_curl_request($handle);
}
//----######------
//---------
$update = json_decode(file_get_contents('php://input'));
var_dump($update);
//=========
$message = $update->message;
$chat_id = $update->message->chat->id;
$message_id = $update->message->message_id;
$from_id = $update->message->from->id;
$name = $update->message->from->first_name;
 $type2 = $update->message->chat->type;
$username = $update->message->from->username;
$gpname = $update->message->chat->title;
$textmessage = isset($update->message->text)?$update->message->text:'';
$txtmsg = $update->message->text;
$replytext = $update->message->reply_to_message->text;
$reply = $update->message->reply_to_message->from->id;
$reply2 = $update->message->reply_to_message->chat->id;
$replyname = $update->message->reply_to_message->from->first_name;
$replyusername = $update->message->reply_to_message->from->username;
$stickerid = $update->message->reply_to_message->sticker->file_id;
$admin = 531608867;
$idbot = 563200077;
$botname = "RTRUBOT",
$botusername = "RTRUBOT";
$botusername2 = "RTRUBOT";
$channel = "joinchat/AAAAAEOUTmy2w5Mf0KNEKA";
$versionbot = "4.7.2";
$forward = $update->message->forward_from;
$photo = $update->message->photo;
$video = $update->message->video;
$location = $update->message->location;
$joinusername = $update->message->new_chat_member->from->username;
$joinmember = $update->message->new_chat_member;
$leftmember = $update->message->left_chat_member;
$sticker = $update->message->sticker;
$document = $update->message->document;
$contact = $update->message->contact;
$game = $update->message->game;
$music = $update->message->audio;
$gif = $update->message->gif;
$voice = $update->message->voice;
$edit = $update->edited_message;
$chatsuper=str_replace("-","",$chat_id);
$step = file_get_contents("step.txt");
 $type = $update->callback_query->message->chat->type;
$from_id2 = $update->callback_query->from->id;
$cblock = $update->callback_query->message->getmember->user;
$token = "".API_KEY."";
$gpname2 = $update->callback_query->message->chat->title;
     $chat_id2 = $update->callback_query->message->chat->id;
    $message_id2 = $update->callback_query->message->message_id;
    $name2 = $update->callback_query->from->first_name;
    $data = $update->callback_query->data;
	$cmember = getChatMembersCount($chat_id2,$token);
$owner = file_get_contents("data/$chat_id/owner.txt");
$modlist = file_get_contents("data/$chat_id/modlist.txt");
$whitelist = file_get_contents("data/$chat_id/whitelist/list.txt");
$whitelist2 = file_get_contents("data/$chat_id2/whitelist/list.txt");
$banlist = file_get_contents("data/$chat_id/banlist/list.txt");
$banlist2 = file_get_contents("data/$chat_id2/banlist/list.txt");
$owner2 = file_get_contents("data/$chat_id2/owner.txt");
$modlist2 = file_get_contents("data/$chat_id2/modlist.txt");

$userlist = file_get_contents("users.txt");
$grouplist = file_get_contents("groups.txt");
$supergrouplist = file_get_contents("supergroups.txt");

$owner3 = file_get_contents("data/$reply2/owner.txt");
$modlist3 = file_get_contents("data/$reply2/modlist.txt");

	$_kick3 = file_get_contents("data/$reply2/settings/kick.txt");
	$_ban3 = file_get_contents("data/$reply2/settings/ban.txt");
	$_unban3 = file_get_contents("data/$reply2/settings/unban.txt");
	$_settings3 = file_get_contents("data/$reply2/settings/settings.txt");
  $_media3 = file_get_contents("data/$reply2/settings/media.txt");
	$_warn3 = file_get_contents("data/$reply2/settings/warn.txt");
	$_muteuser3 = file_get_contents("data/$reply2/settings/muteuser.txt");


$ekhtar = file_get_contents("data/$chat_id/member/$from_id.txt");
$gplist = file_get_contents("data/$chat_id");
$filterlist = file_get_contents("data/$chat_id/settings/filterword.txt");
$filterlist2 = file_get_contents("data/$chat_id2/settings/filterword.txt");
//-------settings
	$muteuserlist = file_get_contents("data/$chat_id/muteuserlist.txt");
	$muteuserlist2 = file_get_contents("data/$chat_id2/muteuserlist.txt");

	$wlctext = file_get_contents("data/$chat_id/gpwlc.txt");
	$wlctext2 = file_get_contents("data/$chat_id2/gpwlc.txt");
	$byetext = file_get_contents("data/$chat_id/gpbye.txt");
	$byetext2 = file_get_contents("data/$chat_id2/gpbye.txt");
	$_bot = file_get_contents("data/$chat_id2/settings/bot.txt");
	$_link = file_get_contents("data/$chat_id2/settings/link.txt");
	$_flood = file_get_contents("data/$chat_id2/settings/flood.txt");
	$_edit = file_get_contents("data/$chat_id2/settings/edit.txt");
	$_web = file_get_contents("data/$chat_id2/settings/web.txt");
	$_num = file_get_contents("data/$chat_id2/settings/num.txt");
	$_chat = file_get_contents("data/$chat_id2/settings/chat.txt");
	$_tag = file_get_contents("data/$chat_id2/settings/tag.txt");
	$_username = file_get_contents("data/$chat_id2/settings/username.txt");
	$_reply = file_get_contents("data/$chat_id2/settings/reply.txt");
	$_lockcmd = file_get_contents("data/$chat_id2/settings/cmd.txt");
	$_fwd = file_get_contents("data/$chat_id2/settings/fwd.txt");
	$_eng = file_get_contents("data/$chat_id2/settings/eng.txt");
	$_arab = file_get_contents("data/$chat_id2/settings/arab.txt");
	$_kickme = file_get_contents("data/$chat_id2/settings/kickme.txt");
	$warnlist2 = file_get_contents("data/$chat_id2/settings/warnlist2.txt");
	$_join= file_get_contents("data/$chat_id2/settings/join.txt");
	$_floods = file_get_contents("data/$chat_id2/settings/floods.txt");

	$warnlists = file_get_contents("data/$chat_id/settings/warnlists.txt");
	$warnlists2 = file_get_contents("data/$chat_id2/settings/warnlists.txt");

	$_contact = file_get_contents("data/$chat_id2/settings/contact.txt");
	$_game = file_get_contents("data/$chat_id2/settings/game.txt");
	$_location = file_get_contents("data/$chat_id2/settings/location.txt");
	$_sticker = file_get_contents("data/$chat_id2/settings/sticker.txt");
	$_photo = file_get_contents("data/$chat_id2/settings/photo.txt");
	$_video = file_get_contents("data/$chat_id2/settings/video.txt");
	$_voice = file_get_contents("data/$chat_id2/settings/voice.txt");
	$_music = file_get_contents("data/$chat_id2/settings/music.txt");
	$_gif = file_get_contents("data/$chat_id2/settings/gif.txt");
	$_document = file_get_contents("data/$chat_id2/settings/document.txt");

	$_kick = file_get_contents("data/$chat_id2/settings/kick.txt");
	$_ban = file_get_contents("data/$chat_id2/settings/ban.txt");
	$_unban = file_get_contents("data/$chat_id2/settings/unban.txt");
	$_settings = file_get_contents("data/$chat_id2/settings/settings.txt");
  $_media = file_get_contents("data/$chat_id2/settings/media.txt");
	$_warn = file_get_contents("data/$chat_id2/settings/warn.txt");
	$_warnsettings = file_get_contents("data/$chat_id2/settings/warnsettings.txt");
  $_warnmedia = file_get_contents("data/$chat_id2/settings/warnmedia.txt");
	$_muteuser = file_get_contents("data/$chat_id2/settings/muteuser.txt");
//-------
	$_lockcmd2 = file_get_contents("data/$chat_id/settings/cmd.txt");
	$_link2 = file_get_contents("data/$chat_id/settings/link.txt");
	$_bot2 = file_get_contents("data/$chat_id/settings/bot.txt");
	$_flood2 = file_get_contents("data/$chat_id/settings/flood.txt");
	$_edit2 = file_get_contents("data/$chat_id/settings/edit.txt");
	$_chat2 = file_get_contents("data/$chat_id/settings/chat.txt");
	$_tag2 = file_get_contents("data/$chat_id/settings/tag.txt");
	$_username2 = file_get_contents("data/$chat_id/settings/username.txt");
	$_fwd2 = file_get_contents("data/$chat_id/settings/fwd.txt");
	$_reply2 = file_get_contents("data/$chat_id/settings/reply.txt");
	$_eng2 = file_get_contents("data/$chat_id/settings/eng.txt");
	$_arab2 = file_get_contents("data/$chat_id/settings/arab.txt");
	$_web2 = file_get_contents("data/$chat_id/settings/web.txt");
	$_num2 = file_get_contents("data/$chat_id/settings/num.txt");
	$_kickme2 = file_get_contents("data/$chat_id/settings/kickme.txt");
	$_join2 = file_get_contents("data/$chat_id/settings/join.txt");
	$_floods2 = file_get_contents("data/$chat_id/settings/floods.txt");

	$_contact2 = file_get_contents("data/$chat_id/settings/contact.txt");
	$_game2 = file_get_contents("data/$chat_id/settings/game.txt");
	$_location2 = file_get_contents("data/$chat_id/settings/location.txt");
	$_sticker2 = file_get_contents("data/$chat_id/settings/sticker.txt");
	$_photo2 = file_get_contents("data/$chat_id/settings/photo.txt");
	$_video2 = file_get_contents("data/$chat_id/settings/video.txt");
	$_voice2 = file_get_contents("data/$chat_id/settings/voice.txt");
	$_music2 = file_get_contents("data/$chat_id/settings/music.txt");
	$_gif2 = file_get_contents("data/$chat_id/settings/gif.txt");
	$_document2 = file_get_contents("data/$chat_id/settings/document.txt");

	$_kick2 = file_get_contents("data/$chat_id/settings/kick.txt");
	$_ban2 = file_get_contents("data/$chat_id/settings/ban.txt");
	$_unban2 = file_get_contents("data/$chat_id/settings/unban.txt");
	$_settings2 = file_get_contents("data/$chat_id/settings/settings.txt");
  $_media2 = file_get_contents("data/$chat_id/settings/media.txt");
	$_muteuser2 = file_get_contents("data/$chat_id/settings/muteuser.txt");
	$_warn2 = file_get_contents("data/$chat_id/settings/warn.txt");
	$_warnsettings2 = file_get_contents("data/$chat_id/settings/warnsettings.txt");
  $_warnmedia2 = file_get_contents("data/$chat_id/settings/warnmedia.txt");
//-------
#$gpsettings = {"$chat_id":{"owner":"".$creator['id']."","modlist":"","filterword":"","whitelist":"","muteuserlist":"","banlist":"","gpwlc":"","gpbye":"","gplink":"","rules":"","botandwarn":{"floods":"5","warnlists":"4","cmd":"❄1�7"},"adminlock":{"warnmedia":"❄1�7","warnsettings":"❄1�7","warn":"❄1�7","unban":"❄1�7","ban":"❄1�7","kick":"❄1�7"},"settings":"❄1�7","media":"❄1�7","gpsettings":{"flood":"✄1�7","link":"✄1�7","join":"❄1�7","username":"❄1�7","tag":"❄1�7","chat":"❄1�7","eng":"❄1�7","fwd":"❄1�7","arab":"❄1�7","web":"❄1�7","num":"❄1�7","reply":"❄1�7","edit":"❄1�7","kickme":"❄1�7","bot":"❄1�7"},"gpmedia":{"gif":"❄1�7","video":"❄1�7","music":"❄1�7","voice":"❄1�7","photo":"❄1�7","sticker":"❄1�7","game":"❄1�7","contact":"❄1�7","document":"❄1�7","location":"❄1�7"}}};
 $gpis = json_decode(file_get_contents("gplist.js"));
 $linkjsa = $gpis->test->gplink;
//-------
function getcreator($chat_id,$token){
  $up = json_decode(file_get_contents('https://api.telegram.org/bot'.$token.'/getChatAdministrators?chat_id='.$chat_id),true);
  $result = $up['result'];
  foreach($result as $key=>$value){
    $found = array_search("creator",$result[$key]);
    if($found !== false){
      return $result[$key]['user'];
    }
  }
}
$creator = getcreator($chat_id,$token);


	$getChatMember = json_decode(file_get_contents("https://api.telegram.org/bot$token/getChatMember?chat_id=$chat_id&user_id=$idbot")); 
    $resultChat = $getChatMember->result;
	$mstatus = $getChatMember->result->status;
function  getUserProfilePhotos($token,$from_id) {
  $url = 'https://api.telegram.org/bot'.$token.'/getUserProfilePhotos?user_id='.$from_id;
  $result = file_get_contents($url);
  $result = json_decode ($result);
  $result = $result->result;
  return $result;
}
$getuserprofile = getUserProfilePhotos($token,$from_id);
$cuphoto = $getuserprofile->total_count;
$getuserphoto = $getuserprofile->photos[0][0]->file_id;

function getChatMembersCount($chat_id,$token) {
  $url = 'https://api.telegram.org/bot'.$token.'/getChatMembersCount?chat_id='.$chat_id;
  $result = file_get_contents($url);
  $result = json_decode ($result);
  $result = $result->result;
  return $result;
}
function SendMessage($ChatId, $TextMsg)
{
 makereq('sendMessage',[
'chat_id'=>$ChatId,
'text'=>$TextMsg,
'parse_mode'=>"MarkDown"
]);
}
function SendMessage2($ChatId, $TextMsg)
{
 makereq('sendMessage',[
'chat_id'=>$ChatId,
'text'=>$TextMsg,
]);
}
function SendSticker($ChatId, $sticker_ID)
{
 makereq('sendSticker',[
'chat_id'=>$ChatId,
'sticker'=>$sticker_ID
]);
}
function Forward($KojaShe,$AzKoja,$KodomMSG)
{
makereq('ForwardMessage',[
'chat_id'=>$KojaShe,
'from_chat_id'=>$AzKoja,
'message_id'=>$KodomMSG
]);
}
function save($filename,$TXTdata)
	{
	$myfile = fopen($filename, "w") or die("Unable to open file!");
	fwrite($myfile, "$TXTdata");
	fclose($myfile);
	}
if($textmessage == "test" && $admin == $from_id){
makereq('sendMessage',[
'chat_id'=>$chat_id,
'text'=>"test: $linkjsa",
]);
}

if($textmessage == "نعم بالتاكيد" && $admin == $from_id || $textmessage == "نعم بالتاكيد" && $owner == $from_id){
mkdir("data/$chat_id");
mkdir("data/$chat_id/settings");
mkdir("data/$chat_id/member");
mkdir("data/$chat_id/banlist");
mkdir("data/$chat_id/whitelist");
save("data/$chat_id/muteuserlist.txt","");
save("data/$chat_id/gpwlc.txt","");
save("data/$chat_id/gpbye.txt","");
save("data/$chat_id/modlist.txt","");
save("data/$chat_id/banlist/list.txt","");
save("data/$chat_id/whitelist/list.txt","");
save("data/$chat_id/gplink.txt","none");
save("data/$chat_id/settings/floods.txt","3");
save("data/$chat_id/settings/warnlists.txt","4");
save("data/$chat_id/rules.txt","none");
save("data/$chat_id/settings/filterword.txt","");
save("data/$chat_id/settings/bot.txt","❌");
save("data/$chat_id/settings/link.txt","✅");
save("data/$chat_id/settings/flood.txt","✅");
save("data/$chat_id/settings/join.txt","❌");
save("data/$chat_id/settings/location.txt","❌");
save("data/$chat_id/settings/username.txt","❌");
save("data/$chat_id/settings/game.txt","❌");
save("data/$chat_id/settings/contact.txt","❌");
save("data/$chat_id/settings/edit.txt","❌");
save("data/$chat_id/settings/tag.txt","❌");
save("data/$chat_id/settings/chat.txt","❌");
save("data/$chat_id/settings/eng.txt","❌");
save("data/$chat_id/settings/fwd.txt","❌");
save("data/$chat_id/settings/kickme.txt","❌");
save("data/$chat_id/settings/reply.txt","❌");
save("data/$chat_id/settings/arab.txt","❌");
save("data/$chat_id/settings/num.txt","❌");
save("data/$chat_id/settings/web.txt","❌");
save("data/$chat_id/settings/sticker.txt","❌");
save("data/$chat_id/settings/photo.txt","❌");
save("data/$chat_id/settings/video.txt","❌");
save("data/$chat_id/settings/voice.txt","❌");
save("data/$chat_id/settings/music.txt","❌");
save("data/$chat_id/settings/gif.txt","❌");
save("data/$chat_id/settings/document.txt","❌");
save("data/$chat_id/settings/settings.txt","❌");
save("data/$chat_id/settings/media.txt","❌");
save("data/$chat_id/settings/ban.txt","❌");
save("data/$chat_id/settings/kick.txt","❌");
save("data/$chat_id/settings/unban.txt","❌");
save("data/$chat_id/settings/warn.txt","❌");
save("data/$chat_id/settings/warnsettings.txt","❌");
save("data/$chat_id/settings/warnmedia.txt","❌");
save("data/$chat_id/settings/muteuser.txt","❌");
save("data/$chat_id/settings/cmd.txt","❌");
makereq('sendMessage',[
'chat_id'=>$chat_id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
}

if($type2 == "group" || $type2 == "supergroup"){
			if (!file_exists("data/$chat_id")) {
mkdir("data/$chat_id");
mkdir("data/$chat_id/settings");
mkdir("data/$chat_id/member");
mkdir("data/$chat_id/banlist");
mkdir("data/$chat_id/whitelist");
save("data/$chat_id/settings/bot.txt","❌");
save("data/$chat_id/gpwlc.txt","");
save("data/$chat_id/gpbye.txt","");
save("data/$chat_id/modlist.txt","");
save("data/$chat_id/settings/floods.txt","3");
save("data/$chat_id/banlist/list.txt","");
save("data/$chat_id/whitelist/list.txt","");
save("data/$chat_id/gplink.txt","none");
save("data/$chat_id/settings/warnlists.txt","4");
save("data/$chat_id/settings/modlist.txt","");
save("data/$chat_id/rules.txt","none");
save("data/$chat_id/settings/filterword.txt","");
save("data/$chat_id/settings/link.txt","✅");
save("data/$chat_id/settings/flood.txt","✅");
save("data/$chat_id/settings/join.txt","❌");
save("data/$chat_id/settings/location.txt","❌");
save("data/$chat_id/settings/username.txt","❌");
save("data/$chat_id/settings/game.txt","❌");
save("data/$chat_id/settings/contact.txt","❌");
save("data/$chat_id/settings/edit.txt","❌");
save("data/$chat_id/settings/tag.txt","❌");
save("data/$chat_id/settings/chat.txt","❌");
save("data/$chat_id/settings/eng.txt","❌");
save("data/$chat_id/settings/fwd.txt","❌");
save("data/$chat_id/settings/kickme.txt","❌");
save("data/$chat_id/settings/reply.txt","❌");
save("data/$chat_id/settings/arab.txt","❌");
save("data/$chat_id/settings/num.txt","❌");
save("data/$chat_id/settings/web.txt","❌");
save("data/$chat_id/settings/sticker.txt","❌");
save("data/$chat_id/settings/photo.txt","❌");
save("data/$chat_id/settings/video.txt","❌");
save("data/$chat_id/settings/voice.txt","❌");
save("data/$chat_id/settings/music.txt","❌");
save("data/$chat_id/settings/gif.txt","❌");
save("data/$chat_id/settings/document.txt","❌");
save("data/$chat_id/settings/settings.txt","❌");
save("data/$chat_id/settings/media.txt","❌");
save("data/$chat_id/settings/ban.txt","❌");
save("data/$chat_id/settings/kick.txt","❌");
save("data/$chat_id/settings/unban.txt","❌");
save("data/$chat_id/settings/warn.txt","❌");
save("data/$chat_id/settings/warnsettings.txt","❌");
save("data/$chat_id/settings/warnmedia.txt","❌");
save("data/$chat_id/settings/bot.txt","❌");
}
				if (!file_exists("data/$chat_id/muteuserlist.txt")) {
					save("data/$chat_id/muteuserlist.txt","");
		}
					if (!file_exists("data/$chat_id/settings/muteuser.txt")) {
	save("data/$chat_id/settings/muteuser.txt","❌");
		}
					if (!file_exists("data/$chat_id/settings/cmd.txt")) {
save("data/$chat_id/settings/cmd.txt","❌");
		}
}

		if ($type2 == "group") {
	 if (strpos($grouplist , "$chat_id") == false){
 $txxt = file_get_contents('groups.txt');
    $pmembersid= explode("\n",$txxt);
    if (!in_array($chat_id,$pmembersid)){
      $aaddd = file_get_contents('groups.txt');
      $aaddd .= $chat_id."\n";
  file_put_contents('groups.txt',$aaddd);
    }
	}
}
		if ($type2 == "supergroup") {
	 if (strpos($supergrouplist , "$chat_id") == false){
 $txxt = file_get_contents('supergroups.txt');
    $pmembersid= explode("\n",$txxt);
    if (!in_array($chat_id,$pmembersid)){
      $aaddd = file_get_contents('supergroups.txt');
      $aaddd .= $chat_id."\n";
  file_put_contents('supergroups.txt',$aaddd);
    }
	}
}

		if ($type2 == "supergroup" || $type2 == "group") {
			if (!file_exists("data/$chat_id/owner.txt")) {
	save("data/$chat_id/owner.txt","".$creator['id']."");
			}
    }

		if ( strpos($textmessage , "/") !== false  && $mstatus != "administrator" || strpos($textmessage , "!") !== false  && $mstatus != "administrator" || strpos($textmessage , "#") !== false && $mstatus != "administrator" ) {
	     if ($owner == $from_id || $admin == $from_id || strpos($modlist , "$from_id") !== false) {
if ($type2 == "supergroup" || $type2 == "group") {
	var_dump(makereq('sendMessage',[
            'chat_id'=>$chat_id,
  "text" => '',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'','callback_data'=>'nasbiosgp'],['text'=>'','callback_data'=>'nasbandroidgp'],
]
]
			])
		]));
    }
			 }
		}

   if($data == "closetab" ){
		if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false){
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- تم تنفيذ طلبك بنجاح ✅ -',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'Closed','callback_data'=>'ش'],
]
]
			])
		]));
			}
	 }

		if ($type2 == "channel") {
makereq('leaveChat',[
	'chat_id'=>$chat_id
	]);
	}

    if($data == "group_media" ){
			if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false){
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'⚡️ الملصقات','callback_data'=>'nolock'],['text'=>$_sticker,'callback_data'=>'lock_sticker']
],
[
  ['text'=>'⚡️ الصور','callback_data'=>'nolock'],['text'=>$_photo,'callback_data'=>'lock_photo']
],
[
  ['text'=>'⚡️ الفيديو','callback_data'=>'nolock'],['text'=>$_video,'callback_data'=>'lock_video']
],
	[
  ['text'=>'⚡️ الصوت','callback_data'=>'nolock'],['text'=>$_voice,'callback_data'=>'lock_voice']
],
	[
  ['text'=>'⚡️ الموسيقى','callback_data'=>'nolock'],['text'=>$_music,'callback_data'=>'lock_music']
],
[
  ['text'=>'⚡️ المتحركه','callback_data'=>'nolock'],['text'=>$_gif,'callback_data'=>'lock_gif']
],
[
  ['text'=>'⚡️ الكلايش ','callback_data'=>'nolock'],['text'=>$_document,'callback_data'=>'lock_document']
],
[
  ['text'=>'⚡️ المواقع ','callback_data'=>'nolock'],['text'=>$_location,'callback_data'=>'lock_location']
],
[
  ['text'=>'⚡️ الجهات ','callback_data'=>'nolock'],['text'=>$_contact,'callback_data'=>'lock_contact']
],
[
  ['text'=>'⚡️ الالعاب ','callback_data'=>'nolock'],['text'=>$_game,'callback_data'=>'lock_game']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

  if($data == "reStArT" ){
			if($admin == $from_id2 || $owner2 == $from_id2){
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
'text'=>"- لاعادة تعيين ضبط الاعدادات ارسل ⚠️ -
- ( نعم بالتاكيد ) 📬 •",
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
	}
}

if ($textmessage == 'الاوامر الشفافه' || $textmessage == 'شفاف' || $textmessage == 'م6' ) {
if( $admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false ){
	var_dump(makereq('sendMessage',[
  'chat_id' => $update->message->chat->id,
  "text" => 'حسنا عزيزي ♦️ اختر احد الازرار ⚡️ التي في الاسفل 🌟
           ֆ • • • • • • • • • • • • • • • • ֆ
[- اضغط هنا وتابع قناة البوت ⚠️](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
  'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id,
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'• الاعدادات 🏴 •','callback_data'=>'group_settings'],
],
[
  ['text'=>'• الميديا 🔖 •','callback_data'=>'group_media'],
],
[
  ['text'=>'• التكرار والتحذير ⚠️ •','callback_data'=>'floodandwarn'],
],
[
  ['text'=>'• اعدادات القفل ⚙️ •','callback_data'=>'adminlock'],
],
[
  ['text'=>'• معلومات المجموعة 🔱 •','callback_data'=>'gpinfo'],
],
[
  ['text'=>'• اعادة ضبط الاعدادات ♻️ •','callback_data'=>'reStArT'],
],
[
  ['text'=>'• خروج 📬 •','callback_data'=>'closetab'],
],
		[
  ['text'=>'- اضغط هنا وتابع جديدنا ✅ -','url'=>'https://telegram.me/'.$channel.''],
]
]
			])
		]));
	
	}
}
   if($data == "settings" ){
			if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false){
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => 'حسنا عزيزي ♦️ اختر احد الازرار ⚡️ التي في الاسفل 🌟
                 ֆ • • • • • • • • • • • • • • • • ֆ
[- اضغط هنا وتابع قناة البوت ⚠️](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id,
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'• الاعدادات 🏴 •','callback_data'=>'group_settings'],
],
[
  ['text'=>'• الميديا 🔖 •','callback_data'=>'group_media'],
],
[
  ['text'=>'• التكرار والتحذير ⚠️ •','callback_data'=>'floodandwarn'],
],
[
  ['text'=>'• اعدادات القفل ⚙️ •','callback_data'=>'adminlock'],
],
[
  ['text'=>'• معلومات المجموعة 🔱 •','callback_data'=>'gpinfo'],
],
[
  ['text'=>'• اعادة ضبط الاعدادات ♻️ •','callback_data'=>'reStArT'],
],
[
  ['text'=>'• خروج 📬 •','callback_data'=>'closetab'],
],
		[
  ['text'=>'- اضغط هنا وتابع جديدنا ✅ -','url'=>'https://telegram.me/'.$channel.''],
]
]
			])
		]));
				}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}
    if($data == "adminlock" ){
				if($admin == $from_id2 || $owner2 == $from_id2){
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'• قفل الطرد 📃 •','callback_data'=>'nolock'],['text'=>$_kick,'callback_data'=>'lock_kick']
],
[
  ['text'=>'• قفل الحظر 📃 •','callback_data'=>'nolock'],['text'=>$_ban,'callback_data'=>'lock_ban']
],
[
  ['text'=>'• قفل فتح الحظر 📃 •','callback_data'=>'nolock'],['text'=>$_unban,'callback_data'=>'lock_unban']
],
[
  ['text'=>'• قفل الكتم 📃 •','callback_data'=>'nolock'],['text'=>$_muteuser,'callback_data'=>'lock_muteuser']
],
[
  ['text'=>'• قفل الاعدادات 📃 •','callback_data'=>'nolock'],['text'=>$_settings,'callback_data'=>'lock_settings']
],
[
  ['text'=>'• قفل الميديا 📃 •','callback_data'=>'nolock'],['text'=>$_media,'callback_data'=>'lock_media']
],
[
  ['text'=>'• قفل التحذير 📃 •','callback_data'=>'nolock'],['text'=>$_warn,'callback_data'=>'lock_warn']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
				}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- هناكك خطا ⚠️ -",
]);
		}
	}

    if($data == "floodandwarn" ){
			if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_settings == "✅"){
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- اهلا بك عزيزي في اوامر التكرار والتحذير 🏴 -
          ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
	[
  ['text'=>'- قفل هذه الاوامر 👇🏿 -','callback_data'=>'nolock'],['text'=>$_lockcmd,'callback_data'=>'lock_cmd']
],
[
  ['text'=>'• عدد التكرار ↘️ •','callback_data'=>'nolock'],
],
[
  ['text'=>'🔻','callback_data'=>'minflood'],['text'=>$_floods,'callback_data'=>'flood'],['text'=>'🔺','callback_data'=>'maxflood'],
],
[
  ['text'=>'• عدد التحذير ↘️ •','callback_data'=>'nolock'],
],
[
  ['text'=>'🔻','callback_data'=>'minwarn'],['text'=>$warnlists2,'callback_data'=>'warn'],['text'=>'🔺','callback_data'=>'maxwarn'],
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

    if($data == "filterlist" ){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false){
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => 'Filter List:
'.$filterlist2.'',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
				}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

    if($data == "whitelist" ){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false){
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => 'White List:
'.$whitelist2.'',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
				}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}


    if($data == "muteuserlist" ){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false){
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => 'MuteUser List:
'.$muteuserlist2.'',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
				}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

    if($data == "banlist" ){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false){
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => 'Ban List:
'.$banlist2.'',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
				}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

    if($data == "gpinfo"){
			if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false){
			var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- معلومات المجموعةه 🏴 الخاصةه بك هي 📬 -',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'- معلومات المجموعةه 🏴 -','callback_data'=>'a'],
],
	[
  ['text'=>'• ايدي المجموعةه 📃 •','callback_data'=>'a'],['text'=>"$chat_id2",'callback_data'=>'a'],
],
	[
  ['text'=>'• اسم المجموعةه ⚠️ •','callback_data'=>'a'],['text'=>"$gpname2",'callback_data'=>'a'],
],
	[
  ['text'=>'• نوع المجموعةه 📬 •','callback_data'=>'a'],['text'=>"$type",'callback_data'=>'a'],
],
	[
  ['text'=>'• اعضاء المجموعةه 💬 •','callback_data'=>'a'],['text'=> "$cmember",'callback_data'=>'a'],
],
	[
  ['text'=>'• رسائل المجموعةه 🍥 •','callback_data'=>'a'],['text'=> "$message_id2",'callback_data'=>'a'],
],
	[
  ['text'=>'- تحديث المعلومات 🔄 •','callback_data'=>'gpinfo2'],
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
					}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

    if($data == "gpinfo2"){
			if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false){
			var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- معلومات المجموعةه 🏴 الخاصةه بك هي 📬 -',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'- معلومات المجموعةه 🏴 -','callback_data'=>'a'],
],
	[
  ['text'=>'• ايدي المجموعةه 📃 •','callback_data'=>'a'],['text'=>"$chat_id2",'callback_data'=>'a'],
],
	[
  ['text'=>'• اسم المجموعةه ⚠️ •','callback_data'=>'a'],['text'=>"$gpname2",'callback_data'=>'a'],
],
	[
  ['text'=>'• نوع المجموعةه 📬 •','callback_data'=>'a'],['text'=>"$type",'callback_data'=>'a'],
],
	[
  ['text'=>'• اعضاء المجموعةه 💬 •','callback_data'=>'a'],['text'=> "$cmember",'callback_data'=>'a'],
],
	[
  ['text'=>'• رسائل المجموعةه 🍥 •','callback_data'=>'a'],['text'=> "$message_id2",'callback_data'=>'a'],
],
	[
  ['text'=>'- تحديث المعلومات 🔄 •','callback_data'=>'gpinfo'],
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
					}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}


    if($data == "group_settings"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false){
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'🏷 التكرار','callback_data'=>'nolock'],['text'=>$_flood,'callback_data'=>'lock_flood']
],
[
  ['text'=>'🏷 الروابط','callback_data'=>'nolock'],['text'=>$_link,'callback_data'=>'lock_links']
],
[
  ['text'=>'🏷 التاك','callback_data'=>'nolock'],['text'=>$_tag,'callback_data'=>'lock_tag']
],
[
  ['text'=>'🏷 المعرف','callback_data'=>'nolock'],['text'=>$_username,'callback_data'=>'lock_username']
],
[
  ['text'=>'🏷 الارقام','callback_data'=>'nolock'],['text'=>$_num,'callback_data'=>'lock_number']
],
[
  ['text'=>'🏷 الويب','callback_data'=>'nolock'],['text'=>$_web,'callback_data'=>'lock_web']
],
[
  ['text'=>'🏷 الدردشه','callback_data'=>'nolock'],['text'=>$_chat,'callback_data'=>'lock_chat']
],
[
  ['text'=>'🏷 التوجيه','callback_data'=>'nolock'],['text'=>$_fwd,'callback_data'=>'lock_fwd']
],
[
  ['text'=>'🏷 الرد','callback_data'=>'nolock'],['text'=>$_reply,'callback_data'=>'lock_reply']
],
[
  ['text'=>'🏷 التعديل','callback_data'=>'nolock'],['text'=>$_edit,'callback_data'=>'lock_edit']
],
[
  ['text'=>'🏷 الانجليزية','callback_data'=>'nolock'],['text'=>$_eng,'callback_data'=>'lock_eng']
],
[
  ['text'=>'🏷 العربية','callback_data'=>'nolock'],['text'=>$_arab,'callback_data'=>'lock_arab']
],
[
  ['text'=>'🏷 الانضمام','callback_data'=>'nolock'],['text'=>$_join,'callback_data'=>'lock_join']
],
[
  ['text'=>'🏷 البوتات','callback_data'=>'nolock'],['text'=>$_bot,'callback_data'=>'lock_bots']
],
	[
  ['text'=>'🏷 المغادرة','callback_data'=>'nolock'],['text'=>$_kickme,'callback_data'=>'lock_kickme']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}
//----------Flood and Warn settings----------\\
    if($data == "minflood"){	
   if($admin == $from_id2 || $owner2 == $from_id2 ){
if($_floods == 3){
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>" اختر من 1 الى 15 لايمكنك تحديد اكثر 🏷",
]);
		}
if($_floods > 3){
$setflood = $_floods - 1;
save("data/$chat_id2/settings/floods.txt","$setflood");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- اهلا بك عزيزي في اوامر التكرار والتحذير 🏴 -
          ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
	[
  ['text'=>'- قفل هذه الاوامر 👇🏿 -','callback_data'=>'nolock'],['text'=>$_lockcmd,'callback_data'=>'lock_cmd']
],
[
  ['text'=>'• عدد التكرار ↘️ •','callback_data'=>'nolock'],
],
[
  ['text'=>'🔻','callback_data'=>'minflood'],['text'=>"$setflood",'callback_data'=>'flood'],['text'=>'🔺','callback_data'=>'maxflood'],
],
[
  ['text'=>'• عدد التحذير ↘️ •','callback_data'=>'nolock'],
],
[
  ['text'=>'🔻','callback_data'=>'minwarn'],['text'=>$warnlists2,'callback_data'=>'warn'],['text'=>'🔺','callback_data'=>'maxwarn'],
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}
}

    if($data == "maxflood"){	
   if($admin == $from_id2 || $owner2 == $from_id2 ){
if($_floods == 15){
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>" اختر من 1 الى 15 لايمكنك تحديد اكثر 🏷",
]);
		}
if($_floods < 15){
$setflood = $_floods + 1;
save("data/$chat_id2/settings/floods.txt","$setflood");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- اهلا بك عزيزي في اوامر التكرار والتحذير 🏴 -
          ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
	[
  ['text'=>'- قفل هذه الاوامر 👇🏿 -','callback_data'=>'nolock'],['text'=>$_lockcmd,'callback_data'=>'lock_cmd']
],
[
  ['text'=>'• عدد التكرار ↘️ •','callback_data'=>'nolock'],
],
[
  ['text'=>'🔻','callback_data'=>'minflood'],['text'=>"$setflood",'callback_data'=>'flood'],['text'=>'🔺','callback_data'=>'maxflood'],
],
[
  ['text'=>'• عدد التحذير ↘️ •','callback_data'=>'nolock'],
],
[
  ['text'=>'🔻','callback_data'=>'minwarn'],['text'=>$warnlists2,'callback_data'=>'warn'],['text'=>'🔺','callback_data'=>'maxwarn'],
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}
}


    if($data == "minwarn"){	
   if($admin == $from_id2 || $owner2 == $from_id2 ){
if($warnlists2 == 1){
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>" اختر من 1 الى 15 لايمكنك تحديد اكثر 🏷",
]);
		}
if($warnlists2 > 1){
$setwarn = $warnlists2 - 1;
save("data/$chat_id2/settings/warnlists.txt","$setwarn");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- اهلا بك عزيزي في اوامر التكرار والتحذير 🏴 -
          ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
	[
  ['text'=>'- قفل هذه الاوامر 👇🏿 -','callback_data'=>'nolock'],['text'=>$_lockcmd,'callback_data'=>'lock_cmd']
],
[
  ['text'=>'• عدد التكرار ↘️ •','callback_data'=>'nolock'],
],
[
  ['text'=>'🔻','callback_data'=>'minflood'],['text'=>$_floods,'callback_data'=>'flood'],['text'=>'🔺','callback_data'=>'maxflood'],
],
[
  ['text'=>'• عدد التحذير ↘️ •','callback_data'=>'nolock'],
],
[
  ['text'=>'🔻','callback_data'=>'minwarn'],['text'=>"$setwarn",'callback_data'=>'warn'],['text'=>'🔺','callback_data'=>'maxwarn'],
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}
}

    if($data == "maxwarn"){	
   if($admin == $from_id2 || $owner2 == $from_id2 ){
if($warnlists2 == 9){
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>" اختر من 1 الى 15 لايمكنك تحديد اكثر 🏷",
]);
		}
if($warnlists2 < 9){
$setwarn = $warnlists2 + 1;
save("data/$chat_id2/settings/warnlists.txt","$setwarn");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- اهلا بك عزيزي في اوامر التكرار والتحذير 🏴 -
          ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
	[
  ['text'=>'- قفل هذه الاوامر 👇🏿 -','callback_data'=>'nolock'],['text'=>$_lockcmd,'callback_data'=>'lock_cmd']
],
[
  ['text'=>'• عدد التكرار ↘️ •','callback_data'=>'nolock'],
],
[
  ['text'=>'🔻','callback_data'=>'minflood'],['text'=>$_floods,'callback_data'=>'flood'],['text'=>'🔺','callback_data'=>'maxflood'],
],
[
  ['text'=>'• عدد التحذير ↘️ •','callback_data'=>'nolock'],
],
[
  ['text'=>'🔻','callback_data'=>'minwarn'],['text'=>"$setwarn",'callback_data'=>'warn'],['text'=>'🔺','callback_data'=>'maxwarn'],
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}
}

  if($data == "lock_cmd" && $_lockcmd == "❌"){
				if($admin == $from_id2 || $owner2 == $from_id2){
save("data/$chat_id2/settings/cmd.txt","✅");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- اهلا بك عزيزي في اوامر التكرار والتحذير 🏴 -
          ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
	[
  ['text'=>'- قفل هذه الاوامر 👇🏿 -','callback_data'=>'nolock'],['text'=>"✅",'callback_data'=>'lock_cmd']
],
[
  ['text'=>'• عدد التكرار ↘️ •','callback_data'=>'nolock'],
],
[
  ['text'=>'🔻','callback_data'=>'minflood'],['text'=>$_floods,'callback_data'=>'flood'],['text'=>'🔺','callback_data'=>'maxflood'],
],
[
  ['text'=>'• عدد التحذير ↘️ •','callback_data'=>'nolock'],
],
[
  ['text'=>'🔻','callback_data'=>'minwarn'],['text'=>"$warnlists2",'callback_data'=>'warn'],['text'=>'🔺','callback_data'=>'maxwarn'],
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- هناكك خطا ⚠️ -",
]);
		}
	}

  if($data == "lock_cmd" && $_lockcmd == "✅"){
				if($admin == $from_id2 || $owner2 == $from_id2 ){
save("data/$chat_id2/settings/cmd.txt","❌");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- اهلا بك عزيزي في اوامر التكرار والتحذير 🏴 -
          ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
	[
  ['text'=>'- قفل هذه الاوامر 👇🏿 -','callback_data'=>'nolock'],['text'=>"❌",'callback_data'=>'lock_cmd']
],
[
  ['text'=>'• عدد التكرار ↘️ •','callback_data'=>'nolock'],
],
[
  ['text'=>'🔻','callback_data'=>'minflood'],['text'=>$_floods,'callback_data'=>'flood'],['text'=>'🔺','callback_data'=>'maxflood'],
],
[
  ['text'=>'• عدد التحذير ↘️ •','callback_data'=>'nolock'],
],
[
  ['text'=>'🔻','callback_data'=>'minwarn'],['text'=>"$warnlists2",'callback_data'=>'warn'],['text'=>'🔺','callback_data'=>'maxwarn'],
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- هناكك خطا ⚠️ -",
]);
		}
	}

//----------lock and unlock admin settings----------\\
  if($data == "lock_kick" && $_kick == "❌"){
				if($admin == $from_id2 || $owner2 == $from_id2){
save("data/$chat_id2/settings/kick.txt","✅");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'• قفل الطرد 📃 •','callback_data'=>'nolock'],['text'=>"✅",'callback_data'=>'lock_kick']
],
[
  ['text'=>'• قفل الحظر 📃 •','callback_data'=>'nolock'],['text'=>$_ban,'callback_data'=>'lock_ban']
],
[
  ['text'=>'• قفل فتح الحظر 📃 •','callback_data'=>'nolock'],['text'=>$_unban,'callback_data'=>'lock_unban']
],
[
  ['text'=>'• قفل الكتم 📃 •','callback_data'=>'nolock'],['text'=>$_muteuser,'callback_data'=>'lock_muteuser']
],
[
  ['text'=>'• قفل الاعدادات 📃 •','callback_data'=>'nolock'],['text'=>$_settings,'callback_data'=>'lock_settings']
],
[
  ['text'=>'• قفل الميديا 📃 •','callback_data'=>'nolock'],['text'=>$_media,'callback_data'=>'lock_media']
],
[
  ['text'=>'• قفل التحذير 📃 •','callback_data'=>'nolock'],['text'=>$_warn,'callback_data'=>'lock_warn']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- هناكك خطا ⚠️ -",
]);
		}
	}

  if($data == "lock_kick" && $_kick == "✅"){
				if($admin == $from_id2 || $owner2 == $from_id2 ){
save("data/$chat_id2/settings/kick.txt","❌");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'• قفل الطرد 📃 •','callback_data'=>'nolock'],['text'=>"❌",'callback_data'=>'lock_kick']
],
[
  ['text'=>'• قفل الحظر 📃 •','callback_data'=>'nolock'],['text'=>$_ban,'callback_data'=>'lock_ban']
],
[
  ['text'=>'• قفل فتح الحظر 📃 •','callback_data'=>'nolock'],['text'=>$_unban,'callback_data'=>'lock_unban']
],
[
  ['text'=>'• قفل الكتم 📃 •','callback_data'=>'nolock'],['text'=>$_muteuser,'callback_data'=>'lock_muteuser']
],
[
  ['text'=>'• قفل الاعدادات 📃 •','callback_data'=>'nolock'],['text'=>$_settings,'callback_data'=>'lock_settings']
],
[
  ['text'=>'• قفل الميديا 📃 •','callback_data'=>'nolock'],['text'=>$_media,'callback_data'=>'lock_media']
],
[
  ['text'=>'• قفل التحذير 📃 •','callback_data'=>'nolock'],['text'=>$_warn,'callback_data'=>'lock_warn']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- هناكك خطا ⚠️ -",
]);
		}
	}


  if($data == "lock_ban" && $_ban == "❌"){
				if($admin == $from_id2 || $owner2 == $from_id2 ){
save("data/$chat_id2/settings/ban.txt","✅");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'• قفل الطرد 📃 •','callback_data'=>'nolock'],['text'=>$_kick,'callback_data'=>'lock_kick']
],
[
  ['text'=>'• قفل الحظر 📃 •','callback_data'=>'nolock'],['text'=>"✅",'callback_data'=>'lock_ban']
],
[
  ['text'=>'• قفل فتح الحظر 📃 •','callback_data'=>'nolock'],['text'=>$_unban,'callback_data'=>'lock_unban']
],
[
  ['text'=>'• قفل الكتم 📃 •','callback_data'=>'nolock'],['text'=>$_muteuser,'callback_data'=>'lock_muteuser']
],
[
  ['text'=>'• قفل الاعدادات 📃 •','callback_data'=>'nolock'],['text'=>$_settings,'callback_data'=>'lock_settings']
],
[
  ['text'=>'• قفل الميديا 📃 •','callback_data'=>'nolock'],['text'=>$_media,'callback_data'=>'lock_media']
],
[
  ['text'=>'• قفل التحذير 📃 •','callback_data'=>'nolock'],['text'=>$_warn,'callback_data'=>'lock_warn']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- هناكك خطا ⚠️ -",
]);
		}
	}

  if($data == "lock_ban" && $_ban == "✅"){
				if($admin == $from_id2 || $owner2 == $from_id2 ){
save("data/$chat_id2/settings/ban.txt","❌");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'• قفل الطرد 📃 •','callback_data'=>'nolock'],['text'=>$_kick,'callback_data'=>'lock_kick']
],
[
  ['text'=>'• قفل الحظر 📃 •','callback_data'=>'nolock'],['text'=>"❌",'callback_data'=>'lock_ban']
],
[
  ['text'=>'• قفل فتح الحظر 📃 •','callback_data'=>'nolock'],['text'=>$_unban,'callback_data'=>'lock_unban']
],
[
  ['text'=>'• قفل الكتم 📃 •','callback_data'=>'nolock'],['text'=>$_muteuser,'callback_data'=>'lock_muteuser']
],
[
  ['text'=>'• قفل الاعدادات 📃 •','callback_data'=>'nolock'],['text'=>$_settings,'callback_data'=>'lock_settings']
],
[
  ['text'=>'• قفل الميديا 📃 •','callback_data'=>'nolock'],['text'=>$_media,'callback_data'=>'lock_media']
],
[
  ['text'=>'• قفل التحذير 📃 •','callback_data'=>'nolock'],['text'=>$_warn,'callback_data'=>'lock_warn']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- هناكك خطا ⚠️ -",
]);
		}
	}

 if($data == "lock_unban" && $_unban == "❌"){
				if($admin == $from_id2 || $owner2 == $from_id2){
save("data/$chat_id2/settings/unban.txt","✅");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'• قفل الطرد 📃 •','callback_data'=>'nolock'],['text'=>$_kick,'callback_data'=>'lock_kick']
],
[
  ['text'=>'• قفل الحظر 📃 •','callback_data'=>'nolock'],['text'=>$_ban,'callback_data'=>'lock_ban']
],
[
  ['text'=>'• قفل فتح الحظر 📃 •','callback_data'=>'nolock'],['text'=>"✅",'callback_data'=>'lock_unban']
],
[
  ['text'=>'• قفل الكتم 📃 •','callback_data'=>'nolock'],['text'=>$_muteuser,'callback_data'=>'lock_muteuser']
],
[
  ['text'=>'• قفل الاعدادات 📃 •','callback_data'=>'nolock'],['text'=>$_settings,'callback_data'=>'lock_settings']
],
[
  ['text'=>'• قفل الميديا 📃 •','callback_data'=>'nolock'],['text'=>$_media,'callback_data'=>'lock_media']
],
[
  ['text'=>'• قفل التحذير 📃 •','callback_data'=>'nolock'],['text'=>$_warn,'callback_data'=>'lock_warn']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- هناكك خطا ⚠️ -",
]);
		}
	}

  if($data == "lock_unban" && $_unban == "✅"){
				if($admin == $from_id2 || $owner2 == $from_id2){
save("data/$chat_id2/settings/unban.txt","❌");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'• قفل الطرد 📃 •','callback_data'=>'nolock'],['text'=>$_kick,'callback_data'=>'lock_kick']
],
[
  ['text'=>'• قفل الحظر 📃 •','callback_data'=>'nolock'],['text'=>$_ban,'callback_data'=>'lock_ban']
],
[
  ['text'=>'• قفل فتح الحظر 📃 •','callback_data'=>'nolock'],['text'=>"❌",'callback_data'=>'lock_unban']
],
[
  ['text'=>'• قفل الكتم 📃 •','callback_data'=>'nolock'],['text'=>$_muteuser,'callback_data'=>'lock_muteuser']
],
[
  ['text'=>'• قفل الاعدادات 📃 •','callback_data'=>'nolock'],['text'=>$_settings,'callback_data'=>'lock_settings']
],
[
  ['text'=>'• قفل الميديا 📃 •','callback_data'=>'nolock'],['text'=>$_media,'callback_data'=>'lock_media']
],
[
  ['text'=>'• قفل التحذير 📃 •','callback_data'=>'nolock'],['text'=>$_warn,'callback_data'=>'lock_warn']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- هناكك خطا ⚠️ -",
]);
		}
	}

 if($data == "lock_muteuser" && $_muteuser == "❌"){
				if($admin == $from_id2 || $owner2 == $from_id2){
save("data/$chat_id2/settings/muteuser.txt","✅");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'• قفل الطرد 📃 •','callback_data'=>'nolock'],['text'=>$_kick,'callback_data'=>'lock_kick']
],
[
  ['text'=>'• قفل الحظر 📃 •','callback_data'=>'nolock'],['text'=>$_ban,'callback_data'=>'lock_ban']
],
[
  ['text'=>'• قفل فتح الحظر 📃 •','callback_data'=>'nolock'],['text'=>$_unban,'callback_data'=>'lock_unban']
],
[
  ['text'=>'• قفل الكتم 📃 •','callback_data'=>'nolock'],['text'=>"✅",'callback_data'=>'lock_settings']
],
[
  ['text'=>'• قفل الاعدادات 📃 •','callback_data'=>'nolock'],['text'=>$_settings,'callback_data'=>'lock_settings']
],
[
  ['text'=>'• قفل الميديا 📃 •','callback_data'=>'nolock'],['text'=>$_media,'callback_data'=>'lock_media']
],
[
  ['text'=>'• قفل التحذير 📃 •','callback_data'=>'nolock'],['text'=>$_warn,'callback_data'=>'lock_warn']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- هناكك خطا ⚠️ -",
]);
		}
	}

  if($data == "lock_muteuser" && $_muteuser == "✅"){
				if($admin == $from_id2 || $owner2 == $from_id2){
save("data/$chat_id2/settings/muteuser.txt","❌");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'• قفل الطرد 📃 •','callback_data'=>'nolock'],['text'=>$_kick,'callback_data'=>'lock_kick']
],
[
  ['text'=>'• قفل الحظر 📃 •','callback_data'=>'nolock'],['text'=>$_ban,'callback_data'=>'lock_ban']
],
[
  ['text'=>'• قفل فتح الحظر 📃 •','callback_data'=>'nolock'],['text'=>$_unban,'callback_data'=>'lock_unban']
],
[
  ['text'=>'• قفل الكتم 📃 •','callback_data'=>'nolock'],['text'=>"❌",'callback_data'=>'lock_muteuser']
],
[
  ['text'=>'• قفل الاعدادات 📃 •','callback_data'=>'nolock'],['text'=>$_settings,'callback_data'=>'lock_settings']
],
[
  ['text'=>'• قفل الميديا 📃 •','callback_data'=>'nolock'],['text'=>$_media,'callback_data'=>'lock_media']
],
[
  ['text'=>'• قفل التحذير 📃 •','callback_data'=>'nolock'],['text'=>$_warn,'callback_data'=>'lock_warn']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- هناكك خطا ⚠️ -",
]);
		}
	}

 if($data == "lock_settings" && $_settings == "❌"){
				if($admin == $from_id2 || $owner2 == $from_id2 ){
save("data/$chat_id2/settings/settings.txt","✅");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'• قفل الطرد 📃 •','callback_data'=>'nolock'],['text'=>$_kick,'callback_data'=>'lock_kick']
],
[
  ['text'=>'• قفل الحظر 📃 •','callback_data'=>'nolock'],['text'=>$_ban,'callback_data'=>'lock_ban']
],
[
  ['text'=>'• قفل فتح الحظر 📃 •','callback_data'=>'nolock'],['text'=>$_unban,'callback_data'=>'lock_unban']
],
[
  ['text'=>'• قفل الكتم 📃 •','callback_data'=>'nolock'],['text'=>$_muteuser,'callback_data'=>'lock_muteuser']
],
[
  ['text'=>'• قفل الاعدادات 📃 •','callback_data'=>'nolock'],['text'=>"✅",'callback_data'=>'lock_settings']
],
[
  ['text'=>'• قفل الميديا 📃 •','callback_data'=>'nolock'],['text'=>$_media,'callback_data'=>'lock_media']
],
[
  ['text'=>'• قفل التحذير 📃 •','callback_data'=>'nolock'],['text'=>$_warn,'callback_data'=>'lock_warn']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- هناكك خطا ⚠️ -",
]);
		}
	}

  if($data == "lock_settings" && $_settings == "✅"){
				if($admin == $from_id2 || $owner2 == $from_id2){
save("data/$chat_id2/settings/settings.txt","❌");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'• قفل الطرد 📃 •','callback_data'=>'nolock'],['text'=>$_kick,'callback_data'=>'lock_kick']
],
[
  ['text'=>'• قفل الحظر 📃 •','callback_data'=>'nolock'],['text'=>$_ban,'callback_data'=>'lock_ban']
],
[
  ['text'=>'• قفل فتح الحظر 📃 •','callback_data'=>'nolock'],['text'=>$_unban,'callback_data'=>'lock_unban']
],
[
  ['text'=>'• قفل الكتم 📃 •','callback_data'=>'nolock'],['text'=>$_muteuser,'callback_data'=>'lock_muteuser']
],
[
  ['text'=>'• قفل الاعدادات 📃 •','callback_data'=>'nolock'],['text'=>"❌",'callback_data'=>'lock_settings']
],
[
  ['text'=>'• قفل الميديا 📃 •','callback_data'=>'nolock'],['text'=>$_media,'callback_data'=>'lock_media']
],
[
  ['text'=>'• قفل التحذير 📃 •','callback_data'=>'nolock'],['text'=>$_warn,'callback_data'=>'lock_warn']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- هناكك خطا ⚠️ -",
]);
		}
	}

 if($data == "lock_media" && $_media == "❌"){
				if($admin == $from_id2 || $owner2 == $from_id2){
save("data/$chat_id2/settings/media.txt","✅");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'• قفل الطرد 📃 •','callback_data'=>'nolock'],['text'=>$_kick,'callback_data'=>'lock_kick']
],
[
  ['text'=>'• قفل الحظر 📃 •','callback_data'=>'nolock'],['text'=>$_ban,'callback_data'=>'lock_ban']
],
[
  ['text'=>'• قفل فتح الحظر 📃 •','callback_data'=>'nolock'],['text'=>$_unban,'callback_data'=>'lock_unban']
],
[
  ['text'=>'• قفل الكتم 📃 •','callback_data'=>'nolock'],['text'=>$_muteuser,'callback_data'=>'lock_muteuser']
],
[
  ['text'=>'• قفل الاعدادات 📃 •','callback_data'=>'nolock'],['text'=>$_settings,'callback_data'=>'lock_settings']
],
[
  ['text'=>'• قفل الميديا 📃 •','callback_data'=>'nolock'],['text'=>"✅",'callback_data'=>'lock_media']
],
[
  ['text'=>'• قفل التحذير 📃 •','callback_data'=>'nolock'],['text'=>$_warn,'callback_data'=>'lock_warn']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- هناكك خطا ⚠️ -",
]);
		}
	}

  if($data == "lock_media" && $_media == "✅"){
				if($admin == $from_id2 || $owner2 == $from_id2){
save("data/$chat_id2/settings/media.txt","❌");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'• قفل الطرد 📃 •','callback_data'=>'nolock'],['text'=>$_kick,'callback_data'=>'lock_kick']
],
[
  ['text'=>'• قفل الحظر 📃 •','callback_data'=>'nolock'],['text'=>$_ban,'callback_data'=>'lock_ban']
],
[
  ['text'=>'• قفل فتح الحظر 📃 •','callback_data'=>'nolock'],['text'=>$_unban,'callback_data'=>'lock_unban']
],
[
  ['text'=>'• قفل الكتم 📃 •','callback_data'=>'nolock'],['text'=>$_muteuser,'callback_data'=>'lock_muteuser']
],
[
  ['text'=>'• قفل الاعدادات 📃 •','callback_data'=>'nolock'],['text'=>$_settings,'callback_data'=>'lock_settings']
],
[
  ['text'=>'• قفل الميديا 📃 •','callback_data'=>'nolock'],['text'=>"❌",'callback_data'=>'lock_media']
],
[
  ['text'=>'• قفل التحذير 📃 •','callback_data'=>'nolock'],['text'=>$_warn,'callback_data'=>'lock_warn']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- هناكك خطا ⚠️ -",
]);
		}
	}

 if($data == "lock_warn" && $_warn == "❌"){
				if($admin == $from_id2 || $owner2 == $from_id2){
save("data/$chat_id2/settings/warn.txt","✅");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'• قفل الطرد 📃 •','callback_data'=>'nolock'],['text'=>$_kick,'callback_data'=>'lock_kick']
],
[
  ['text'=>'• قفل الحظر 📃 •','callback_data'=>'nolock'],['text'=>$_ban,'callback_data'=>'lock_ban']
],
[
  ['text'=>'• قفل فتح الحظر 📃 •','callback_data'=>'nolock'],['text'=>$_unban,'callback_data'=>'lock_unban']
],
[
  ['text'=>'• قفل الكتم 📃 •','callback_data'=>'nolock'],['text'=>$_muteuser,'callback_data'=>'lock_muteuser']
],
[
  ['text'=>'• قفل الاعدادات 📃 •','callback_data'=>'nolock'],['text'=>$_settings,'callback_data'=>'lock_settings']
],
[
  ['text'=>'• قفل الميديا 📃 •','callback_data'=>'nolock'],['text'=>$_media,'callback_data'=>'lock_media']
],
[
  ['text'=>'• قفل التحذير 📃 •','callback_data'=>'nolock'],['text'=>"✅",'callback_data'=>'lock_warn']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- هناكك خطا ⚠️ -",
]);
		}
	}

  if($data == "lock_warn" && $_warn == "✅"){
				if($admin == $from_id2 || $owner2 == $from_id2){
save("data/$chat_id2/settings/warn.txt","❌");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'• قفل الطرد 📃 •','callback_data'=>'nolock'],['text'=>$_kick,'callback_data'=>'lock_kick']
],
[
  ['text'=>'• قفل الحظر 📃 •','callback_data'=>'nolock'],['text'=>$_ban,'callback_data'=>'lock_ban']
],
[
  ['text'=>'• قفل فتح الحظر 📃 •','callback_data'=>'nolock'],['text'=>$_unban,'callback_data'=>'lock_unban']
],
[
  ['text'=>'• قفل الكتم 📃 •','callback_data'=>'nolock'],['text'=>$_muteuser,'callback_data'=>'lock_muteuser']
],
[
  ['text'=>'• قفل الاعدادات 📃 •','callback_data'=>'nolock'],['text'=>$_settings,'callback_data'=>'lock_settings']
],
[
  ['text'=>'• قفل الميديا 📃 •','callback_data'=>'nolock'],['text'=>$_media,'callback_data'=>'lock_media']
],
[
  ['text'=>'• قفل التحذير 📃 •','callback_data'=>'nolock'],['text'=>"❌",'callback_data'=>'lock_warn']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- هناكك خطا ⚠️ -",
]);
		}
	}
//----------lock and unlock by button----------\\
   if($data == "lock_flood" && $_flood == "❌"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_settings == "❌" ){
save("data/$chat_id2/settings/flood.txt","✅");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'🏷 التكرار','callback_data'=>'nolock'],['text'=>"✅",'callback_data'=>'lock_flood']
],
[
  ['text'=>'🏷 الروابط','callback_data'=>'nolock'],['text'=>$_link,'callback_data'=>'lock_links']
],
[
  ['text'=>'🏷 التاك','callback_data'=>'nolock'],['text'=>$_tag,'callback_data'=>'lock_tag']
],
[
  ['text'=>'🏷 المعرف','callback_data'=>'nolock'],['text'=>$_username,'callback_data'=>'lock_username']
],
[
  ['text'=>'🏷 الارقام','callback_data'=>'nolock'],['text'=>$_num,'callback_data'=>'lock_number']
],
[
  ['text'=>'🏷 الويب','callback_data'=>'nolock'],['text'=>$_web,'callback_data'=>'lock_web']
],
[
  ['text'=>'🏷 الدردشه','callback_data'=>'nolock'],['text'=>$_chat,'callback_data'=>'lock_chat']
],
[
  ['text'=>'🏷 التوجيه','callback_data'=>'nolock'],['text'=>$_fwd,'callback_data'=>'lock_fwd']
],
[
  ['text'=>'🏷 الرد','callback_data'=>'nolock'],['text'=>$_reply,'callback_data'=>'lock_reply']
],
[
  ['text'=>'🏷 التعديل','callback_data'=>'nolock'],['text'=>$_edit,'callback_data'=>'lock_edit']
],
[
  ['text'=>'🏷 الانجليزية','callback_data'=>'nolock'],['text'=>$_eng,'callback_data'=>'lock_eng']
],
[
  ['text'=>'🏷 العربية','callback_data'=>'nolock'],['text'=>$_arab,'callback_data'=>'lock_arab']
],
[
  ['text'=>'🏷 الانضمام','callback_data'=>'nolock'],['text'=>$_join,'callback_data'=>'lock_join']
],
[
  ['text'=>'🏷 البوتات','callback_data'=>'nolock'],['text'=>$_bot,'callback_data'=>'lock_bots']
],
	[
  ['text'=>'🏷 المغادرة','callback_data'=>'nolock'],['text'=>$_kickme,'callback_data'=>'lock_kickme']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_flood" && $_flood == "✅"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_settings == "❌"){
save("data/$chat_id2/settings/flood.txt","❌");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'🏷 التكرار','callback_data'=>'nolock'],['text'=>"❌",'callback_data'=>'lock_flood']
],
[
  ['text'=>'🏷 الروابط','callback_data'=>'nolock'],['text'=>$_link,'callback_data'=>'lock_links']
],
[
  ['text'=>'🏷 التاك','callback_data'=>'nolock'],['text'=>$_tag,'callback_data'=>'lock_tag']
],
[
  ['text'=>'🏷 المعرف','callback_data'=>'nolock'],['text'=>$_username,'callback_data'=>'lock_username']
],
[
  ['text'=>'🏷 الارقام','callback_data'=>'nolock'],['text'=>$_num,'callback_data'=>'lock_number']
],
[
  ['text'=>'🏷 الويب','callback_data'=>'nolock'],['text'=>$_web,'callback_data'=>'lock_web']
],
[
  ['text'=>'🏷 الدردشه','callback_data'=>'nolock'],['text'=>$_chat,'callback_data'=>'lock_chat']
],
[
  ['text'=>'🏷 التوجيه','callback_data'=>'nolock'],['text'=>$_fwd,'callback_data'=>'lock_fwd']
],
[
  ['text'=>'🏷 الرد','callback_data'=>'nolock'],['text'=>$_reply,'callback_data'=>'lock_reply']
],
[
  ['text'=>'🏷 التعديل','callback_data'=>'nolock'],['text'=>$_edit,'callback_data'=>'lock_edit']
],
[
  ['text'=>'🏷 الانجليزية','callback_data'=>'nolock'],['text'=>$_eng,'callback_data'=>'lock_eng']
],
[
  ['text'=>'🏷 العربية','callback_data'=>'nolock'],['text'=>$_arab,'callback_data'=>'lock_arab']
],
[
  ['text'=>'🏷 الانضمام','callback_data'=>'nolock'],['text'=>$_join,'callback_data'=>'lock_join']
],
[
  ['text'=>'🏷 البوتات','callback_data'=>'nolock'],['text'=>$_bot,'callback_data'=>'lock_bots']
],
	[
  ['text'=>'🏷 المغادرة','callback_data'=>'nolock'],['text'=>$_kickme,'callback_data'=>'lock_kickme']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_links" && $_link == "❌"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_settings == "❌" ){
save("data/$chat_id2/settings/link.txt","✅");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'🏷 التكرار','callback_data'=>'nolock'],['text'=>$_flood,'callback_data'=>'lock_flood']
],
[
  ['text'=>'🏷 الروابط','callback_data'=>'nolock'],['text'=>"✅",'callback_data'=>'lock_links']
],
[
  ['text'=>'🏷 التاك','callback_data'=>'nolock'],['text'=>$_tag,'callback_data'=>'lock_tag']
],
[
  ['text'=>'🏷 المعرف','callback_data'=>'nolock'],['text'=>$_username,'callback_data'=>'lock_username']
],
[
  ['text'=>'🏷 الارقام','callback_data'=>'nolock'],['text'=>$_num,'callback_data'=>'lock_number']
],
[
  ['text'=>'🏷 الويب','callback_data'=>'nolock'],['text'=>$_web,'callback_data'=>'lock_web']
],
[
  ['text'=>'🏷 الدردشه','callback_data'=>'nolock'],['text'=>$_chat,'callback_data'=>'lock_chat']
],
[
  ['text'=>'🏷 التوجيه','callback_data'=>'nolock'],['text'=>$_fwd,'callback_data'=>'lock_fwd']
],
[
  ['text'=>'🏷 الرد','callback_data'=>'nolock'],['text'=>$_reply,'callback_data'=>'lock_reply']
],
[
  ['text'=>'🏷 التعديل','callback_data'=>'nolock'],['text'=>$_edit,'callback_data'=>'lock_edit']
],
[
  ['text'=>'🏷 الانجليزية','callback_data'=>'nolock'],['text'=>$_eng,'callback_data'=>'lock_eng']
],
[
  ['text'=>'🏷 العربية','callback_data'=>'nolock'],['text'=>$_arab,'callback_data'=>'lock_arab']
],
[
  ['text'=>'🏷 الانضمام','callback_data'=>'nolock'],['text'=>$_join,'callback_data'=>'lock_join']
],
[
  ['text'=>'🏷 البوتات','callback_data'=>'nolock'],['text'=>$_bot,'callback_data'=>'lock_bots']
],
	[
  ['text'=>'🏷 المغادرة','callback_data'=>'nolock'],['text'=>$_kickme,'callback_data'=>'lock_kickme']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_links" && $_link == "✅"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_settings == "❌"){
save("data/$chat_id2/settings/link.txt","❌");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'🏷 التكرار','callback_data'=>'nolock'],['text'=>$_flood,'callback_data'=>'lock_flood']
],
[
  ['text'=>'🏷 الروابط','callback_data'=>'nolock'],['text'=>"❌",'callback_data'=>'lock_links']
],
[
  ['text'=>'🏷 التاك','callback_data'=>'nolock'],['text'=>$_tag,'callback_data'=>'lock_tag']
],
[
  ['text'=>'🏷 المعرف','callback_data'=>'nolock'],['text'=>$_username,'callback_data'=>'lock_username']
],
[
  ['text'=>'🏷 الارقام','callback_data'=>'nolock'],['text'=>$_num,'callback_data'=>'lock_number']
],
[
  ['text'=>'🏷 الويب','callback_data'=>'nolock'],['text'=>$_web,'callback_data'=>'lock_web']
],
[
  ['text'=>'🏷 الدردشه','callback_data'=>'nolock'],['text'=>$_chat,'callback_data'=>'lock_chat']
],
[
  ['text'=>'🏷 التوجيه','callback_data'=>'nolock'],['text'=>$_fwd,'callback_data'=>'lock_fwd']
],
[
  ['text'=>'🏷 الرد','callback_data'=>'nolock'],['text'=>$_reply,'callback_data'=>'lock_reply']
],
[
  ['text'=>'🏷 التعديل','callback_data'=>'nolock'],['text'=>$_edit,'callback_data'=>'lock_edit']
],
[
  ['text'=>'🏷 الانجليزية','callback_data'=>'nolock'],['text'=>$_eng,'callback_data'=>'lock_eng']
],
[
  ['text'=>'🏷 العربية','callback_data'=>'nolock'],['text'=>$_arab,'callback_data'=>'lock_arab']
],
[
  ['text'=>'🏷 الانضمام','callback_data'=>'nolock'],['text'=>$_join,'callback_data'=>'lock_join']
],
[
  ['text'=>'🏷 البوتات','callback_data'=>'nolock'],['text'=>$_bot,'callback_data'=>'lock_bots']
],
	[
  ['text'=>'🏷 المغادرة','callback_data'=>'nolock'],['text'=>$_kickme,'callback_data'=>'lock_kickme']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_tag" && $_tag == "❌"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_settings == "❌"){
save("data/$chat_id2/settings/tag.txt","✅");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'🏷 التكرار','callback_data'=>'nolock'],['text'=>$_flood,'callback_data'=>'lock_flood']
],
[
  ['text'=>'🏷 الروابط','callback_data'=>'nolock'],['text'=>$_link,'callback_data'=>'lock_links']
],
[
  ['text'=>'🏷 التاك','callback_data'=>'nolock'],['text'=>"✅",'callback_data'=>'lock_tag']
],
[
  ['text'=>'🏷 المعرف','callback_data'=>'nolock'],['text'=>$_username,'callback_data'=>'lock_username']
],
[
  ['text'=>'🏷 الارقام','callback_data'=>'nolock'],['text'=>$_num,'callback_data'=>'lock_number']
],
[
  ['text'=>'🏷 الويب','callback_data'=>'nolock'],['text'=>$_web,'callback_data'=>'lock_web']
],
[
  ['text'=>'🏷 الدردشه','callback_data'=>'nolock'],['text'=>$_chat,'callback_data'=>'lock_chat']
],
[
  ['text'=>'🏷 التوجيه','callback_data'=>'nolock'],['text'=>$_fwd,'callback_data'=>'lock_fwd']
],
[
  ['text'=>'🏷 الرد','callback_data'=>'nolock'],['text'=>$_reply,'callback_data'=>'lock_reply']
],
[
  ['text'=>'🏷 التعديل','callback_data'=>'nolock'],['text'=>$_edit,'callback_data'=>'lock_edit']
],
[
  ['text'=>'🏷 الانجليزية','callback_data'=>'nolock'],['text'=>$_eng,'callback_data'=>'lock_eng']
],
[
  ['text'=>'🏷 العربية','callback_data'=>'nolock'],['text'=>$_arab,'callback_data'=>'lock_arab']
],
[
  ['text'=>'🏷 الانضمام','callback_data'=>'nolock'],['text'=>$_join,'callback_data'=>'lock_join']
],
[
  ['text'=>'🏷 البوتات','callback_data'=>'nolock'],['text'=>$_bot,'callback_data'=>'lock_bots']
],
	[
  ['text'=>'🏷 المغادرة','callback_data'=>'nolock'],['text'=>$_kickme,'callback_data'=>'lock_kickme']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_tag" && $_tag == "✅"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_settings == "❌"){
save("data/$chat_id2/settings/tag.txt","❌");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'🏷 التكرار','callback_data'=>'nolock'],['text'=>$_flood,'callback_data'=>'lock_flood']
],
[
  ['text'=>'🏷 الروابط','callback_data'=>'nolock'],['text'=>$_link,'callback_data'=>'lock_links']
],
[
  ['text'=>'🏷 التاك','callback_data'=>'nolock'],['text'=>"❌",'callback_data'=>'lock_tag']
],
[
  ['text'=>'🏷 المعرف','callback_data'=>'nolock'],['text'=>$_username,'callback_data'=>'lock_username']
],
[
  ['text'=>'🏷 الارقام','callback_data'=>'nolock'],['text'=>$_num,'callback_data'=>'lock_number']
],
[
  ['text'=>'🏷 الويب','callback_data'=>'nolock'],['text'=>$_web,'callback_data'=>'lock_web']
],
[
  ['text'=>'🏷 الدردشه','callback_data'=>'nolock'],['text'=>$_chat,'callback_data'=>'lock_chat']
],
[
  ['text'=>'🏷 التوجيه','callback_data'=>'nolock'],['text'=>$_fwd,'callback_data'=>'lock_fwd']
],
[
  ['text'=>'🏷 الرد','callback_data'=>'nolock'],['text'=>$_reply,'callback_data'=>'lock_reply']
],
[
  ['text'=>'🏷 التعديل','callback_data'=>'nolock'],['text'=>$_edit,'callback_data'=>'lock_edit']
],
[
  ['text'=>'🏷 الانجليزية','callback_data'=>'nolock'],['text'=>$_eng,'callback_data'=>'lock_eng']
],
[
  ['text'=>'🏷 العربية','callback_data'=>'nolock'],['text'=>$_arab,'callback_data'=>'lock_arab']
],
[
  ['text'=>'🏷 الانضمام','callback_data'=>'nolock'],['text'=>$_join,'callback_data'=>'lock_join']
],
[
  ['text'=>'🏷 البوتات','callback_data'=>'nolock'],['text'=>$_bot,'callback_data'=>'lock_bots']
],
	[
  ['text'=>'🏷 المغادرة','callback_data'=>'nolock'],['text'=>$_kickme,'callback_data'=>'lock_kickme']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}


   if($data == "lock_username" && $_username == "❌"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_settings == "❌"){
save("data/$chat_id2/settings/username.txt","✅");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'🏷 التكرار','callback_data'=>'nolock'],['text'=>$_flood,'callback_data'=>'lock_flood']
],
[
  ['text'=>'🏷 الروابط','callback_data'=>'nolock'],['text'=>$_link,'callback_data'=>'lock_links']
],
[
  ['text'=>'🏷 التاك','callback_data'=>'nolock'],['text'=>$_tag,'callback_data'=>'lock_tag']
],
[
  ['text'=>'🏷 المعرف','callback_data'=>'nolock'],['text'=>"✅",'callback_data'=>'lock_username']
],
[
  ['text'=>'🏷 الارقام','callback_data'=>'nolock'],['text'=>$_num,'callback_data'=>'lock_number']
],
[
  ['text'=>'🏷 الويب','callback_data'=>'nolock'],['text'=>$_web,'callback_data'=>'lock_web']
],
[
  ['text'=>'🏷 الدردشه','callback_data'=>'nolock'],['text'=>$_chat,'callback_data'=>'lock_chat']
],
[
  ['text'=>'🏷 التوجيه','callback_data'=>'nolock'],['text'=>$_fwd,'callback_data'=>'lock_fwd']
],
[
  ['text'=>'🏷 الرد','callback_data'=>'nolock'],['text'=>$_reply,'callback_data'=>'lock_reply']
],
[
  ['text'=>'🏷 التعديل','callback_data'=>'nolock'],['text'=>$_edit,'callback_data'=>'lock_edit']
],
[
  ['text'=>'🏷 الانجليزية','callback_data'=>'nolock'],['text'=>$_eng,'callback_data'=>'lock_eng']
],
[
  ['text'=>'🏷 العربية','callback_data'=>'nolock'],['text'=>$_arab,'callback_data'=>'lock_arab']
],
[
  ['text'=>'🏷 الانضمام','callback_data'=>'nolock'],['text'=>$_join,'callback_data'=>'lock_join']
],
[
  ['text'=>'🏷 البوتات','callback_data'=>'nolock'],['text'=>$_bot,'callback_data'=>'lock_bots']
],
	[
  ['text'=>'🏷 المغادرة','callback_data'=>'nolock'],['text'=>$_kickme,'callback_data'=>'lock_kickme']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_username" && $_username == "✅"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_settings == "❌"){
save("data/$chat_id2/settings/username.txt","❌");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'🏷 التكرار','callback_data'=>'nolock'],['text'=>$_flood,'callback_data'=>'lock_flood']
],
[
  ['text'=>'🏷 الروابط','callback_data'=>'nolock'],['text'=>$_link,'callback_data'=>'lock_links']
],
[
  ['text'=>'🏷 التاك','callback_data'=>'nolock'],['text'=>$_tag,'callback_data'=>'lock_tag']
],
[
  ['text'=>'🏷 المعرف','callback_data'=>'nolock'],['text'=>"❌",'callback_data'=>'lock_username']
],
[
  ['text'=>'🏷 الارقام','callback_data'=>'nolock'],['text'=>$_num,'callback_data'=>'lock_number']
],
[
  ['text'=>'🏷 الويب','callback_data'=>'nolock'],['text'=>$_web,'callback_data'=>'lock_web']
],
[
  ['text'=>'🏷 الدردشه','callback_data'=>'nolock'],['text'=>$_chat,'callback_data'=>'lock_chat']
],
[
  ['text'=>'🏷 التوجيه','callback_data'=>'nolock'],['text'=>$_fwd,'callback_data'=>'lock_fwd']
],
[
  ['text'=>'🏷 الرد','callback_data'=>'nolock'],['text'=>$_reply,'callback_data'=>'lock_reply']
],
[
  ['text'=>'🏷 التعديل','callback_data'=>'nolock'],['text'=>$_edit,'callback_data'=>'lock_edit']
],
[
  ['text'=>'🏷 الانجليزية','callback_data'=>'nolock'],['text'=>$_eng,'callback_data'=>'lock_eng']
],
[
  ['text'=>'🏷 العربية','callback_data'=>'nolock'],['text'=>$_arab,'callback_data'=>'lock_arab']
],
[
  ['text'=>'🏷 الانضمام','callback_data'=>'nolock'],['text'=>$_join,'callback_data'=>'lock_join']
],
[
  ['text'=>'🏷 البوتات','callback_data'=>'nolock'],['text'=>$_bot,'callback_data'=>'lock_bots']
],
	[
  ['text'=>'🏷 المغادرة','callback_data'=>'nolock'],['text'=>$_kickme,'callback_data'=>'lock_kickme']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_number" && $_num == "❌"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_settings == "❌"){
save("data/$chat_id2/settings/num.txt","✅");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'🏷 التكرار','callback_data'=>'nolock'],['text'=>$_flood,'callback_data'=>'lock_flood']
],
[
  ['text'=>'🏷 الروابط','callback_data'=>'nolock'],['text'=>$_link,'callback_data'=>'lock_links']
],
[
  ['text'=>'🏷 التاك','callback_data'=>'nolock'],['text'=>$_tag,'callback_data'=>'lock_tag']
],
[
  ['text'=>'🏷 المعرف','callback_data'=>'nolock'],['text'=>$_username,'callback_data'=>'lock_username']
],
[
  ['text'=>'🏷 الارقام','callback_data'=>'nolock'],['text'=>"✅",'callback_data'=>'lock_number']
],
[
  ['text'=>'🏷 الويب','callback_data'=>'nolock'],['text'=>$_web,'callback_data'=>'lock_web']
],
[
  ['text'=>'🏷 الدردشه','callback_data'=>'nolock'],['text'=>$_chat,'callback_data'=>'lock_chat']
],
[
  ['text'=>'🏷 التوجيه','callback_data'=>'nolock'],['text'=>$_fwd,'callback_data'=>'lock_fwd']
],
[
  ['text'=>'🏷 الرد','callback_data'=>'nolock'],['text'=>$_reply,'callback_data'=>'lock_reply']
],
[
  ['text'=>'🏷 التعديل','callback_data'=>'nolock'],['text'=>$_edit,'callback_data'=>'lock_edit']
],
[
  ['text'=>'🏷 الانجليزية','callback_data'=>'nolock'],['text'=>$_eng,'callback_data'=>'lock_eng']
],
[
  ['text'=>'🏷 العربية','callback_data'=>'nolock'],['text'=>$_arab,'callback_data'=>'lock_arab']
],
[
  ['text'=>'🏷 الانضمام','callback_data'=>'nolock'],['text'=>$_join,'callback_data'=>'lock_join']
],
[
  ['text'=>'🏷 البوتات','callback_data'=>'nolock'],['text'=>$_bot,'callback_data'=>'lock_bots']
],
	[
  ['text'=>'🏷 المغادرة','callback_data'=>'nolock'],['text'=>$_kickme,'callback_data'=>'lock_kickme']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_number" && $_num == "✅"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_settings == "❌"){
save("data/$chat_id2/settings/num.txt","❌");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'🏷 التكرار','callback_data'=>'nolock'],['text'=>$_flood,'callback_data'=>'lock_flood']
],
[
  ['text'=>'🏷 الروابط','callback_data'=>'nolock'],['text'=>$_link,'callback_data'=>'lock_links']
],
[
  ['text'=>'🏷 التاك','callback_data'=>'nolock'],['text'=>$_tag,'callback_data'=>'lock_tag']
],
[
  ['text'=>'🏷 المعرف','callback_data'=>'nolock'],['text'=>$_username,'callback_data'=>'lock_username']
],
[
  ['text'=>'🏷 الارقام','callback_data'=>'nolock'],['text'=>"❌",'callback_data'=>'lock_number']
],
[
  ['text'=>'🏷 الويب','callback_data'=>'nolock'],['text'=>$_web,'callback_data'=>'lock_web']
],
[
  ['text'=>'🏷 الدردشه','callback_data'=>'nolock'],['text'=>$_chat,'callback_data'=>'lock_chat']
],
[
  ['text'=>'🏷 التوجيه','callback_data'=>'nolock'],['text'=>$_fwd,'callback_data'=>'lock_fwd']
],
[
  ['text'=>'🏷 الرد','callback_data'=>'nolock'],['text'=>$_reply,'callback_data'=>'lock_reply']
],
[
  ['text'=>'🏷 التعديل','callback_data'=>'nolock'],['text'=>$_edit,'callback_data'=>'lock_edit']
],
[
  ['text'=>'🏷 الانجليزية','callback_data'=>'nolock'],['text'=>$_eng,'callback_data'=>'lock_eng']
],
[
  ['text'=>'🏷 العربية','callback_data'=>'nolock'],['text'=>$_arab,'callback_data'=>'lock_arab']
],
[
  ['text'=>'🏷 الانضمام','callback_data'=>'nolock'],['text'=>$_join,'callback_data'=>'lock_join']
],
[
  ['text'=>'🏷 البوتات','callback_data'=>'nolock'],['text'=>$_bot,'callback_data'=>'lock_bots']
],
	[
  ['text'=>'🏷 المغادرة','callback_data'=>'nolock'],['text'=>$_kickme,'callback_data'=>'lock_kickme']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_web" && $_web == "❌"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_settings == "❌"){
save("data/$chat_id2/settings/web.txt","✅");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'🏷 التكرار','callback_data'=>'nolock'],['text'=>$_flood,'callback_data'=>'lock_flood']
],
[
  ['text'=>'🏷 الروابط','callback_data'=>'nolock'],['text'=>$_link,'callback_data'=>'lock_links']
],
[
  ['text'=>'🏷 التاك','callback_data'=>'nolock'],['text'=>$_tag,'callback_data'=>'lock_tag']
],
[
  ['text'=>'🏷 المعرف','callback_data'=>'nolock'],['text'=>$_username,'callback_data'=>'lock_username']
],
[
  ['text'=>'🏷 الارقام','callback_data'=>'nolock'],['text'=>$_num,'callback_data'=>'lock_number']
],
[
  ['text'=>'🏷 الويب','callback_data'=>'nolock'],['text'=>"✅",'callback_data'=>'lock_web']
],
[
  ['text'=>'🏷 الدردشه','callback_data'=>'nolock'],['text'=>$_chat,'callback_data'=>'lock_chat']
],
[
  ['text'=>'🏷 التوجيه','callback_data'=>'nolock'],['text'=>$_fwd,'callback_data'=>'lock_fwd']
],
[
  ['text'=>'🏷 الرد','callback_data'=>'nolock'],['text'=>$_reply,'callback_data'=>'lock_reply']
],
[
  ['text'=>'🏷 التعديل','callback_data'=>'nolock'],['text'=>$_edit,'callback_data'=>'lock_edit']
],
[
  ['text'=>'🏷 الانجليزية','callback_data'=>'nolock'],['text'=>$_eng,'callback_data'=>'lock_eng']
],
[
  ['text'=>'🏷 العربية','callback_data'=>'nolock'],['text'=>$_arab,'callback_data'=>'lock_arab']
],
[
  ['text'=>'🏷 الانضمام','callback_data'=>'nolock'],['text'=>$_join,'callback_data'=>'lock_join']
],
[
  ['text'=>'🏷 البوتات','callback_data'=>'nolock'],['text'=>$_bot,'callback_data'=>'lock_bots']
],
	[
  ['text'=>'🏷 المغادرة','callback_data'=>'nolock'],['text'=>$_kickme,'callback_data'=>'lock_kickme']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_web" && $_web == "✅"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_settings == "❌"){
save("data/$chat_id2/settings/web.txt","❌");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'🏷 التكرار','callback_data'=>'nolock'],['text'=>$_flood,'callback_data'=>'lock_flood']
],
[
  ['text'=>'🏷 الروابط','callback_data'=>'nolock'],['text'=>$_link,'callback_data'=>'lock_links']
],
[
  ['text'=>'🏷 التاك','callback_data'=>'nolock'],['text'=>$_tag,'callback_data'=>'lock_tag']
],
[
  ['text'=>'🏷 المعرف','callback_data'=>'nolock'],['text'=>$_username,'callback_data'=>'lock_username']
],
[
  ['text'=>'🏷 الارقام','callback_data'=>'nolock'],['text'=>$_num,'callback_data'=>'lock_number']
],
[
  ['text'=>'🏷 الويب','callback_data'=>'nolock'],['text'=>"❌",'callback_data'=>'lock_web']
],
[
  ['text'=>'🏷 الدردشه','callback_data'=>'nolock'],['text'=>$_chat,'callback_data'=>'lock_chat']
],
[
  ['text'=>'🏷 التوجيه','callback_data'=>'nolock'],['text'=>$_fwd,'callback_data'=>'lock_fwd']
],
[
  ['text'=>'🏷 الرد','callback_data'=>'nolock'],['text'=>$_reply,'callback_data'=>'lock_reply']
],
[
  ['text'=>'🏷 التعديل','callback_data'=>'nolock'],['text'=>$_edit,'callback_data'=>'lock_edit']
],
[
  ['text'=>'🏷 الانجليزية','callback_data'=>'nolock'],['text'=>$_eng,'callback_data'=>'lock_eng']
],
[
  ['text'=>'🏷 العربية','callback_data'=>'nolock'],['text'=>$_arab,'callback_data'=>'lock_arab']
],
[
  ['text'=>'🏷 الانضمام','callback_data'=>'nolock'],['text'=>$_join,'callback_data'=>'lock_join']
],
[
  ['text'=>'🏷 البوتات','callback_data'=>'nolock'],['text'=>$_bot,'callback_data'=>'lock_bots']
],
	[
  ['text'=>'🏷 المغادرة','callback_data'=>'nolock'],['text'=>$_kickme,'callback_data'=>'lock_kickme']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_chat" && $_chat == "❌"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_settings == "❌"){
save("data/$chat_id2/settings/chat.txt","✅");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'🏷 التكرار','callback_data'=>'nolock'],['text'=>$_flood,'callback_data'=>'lock_flood']
],
[
  ['text'=>'🏷 الروابط','callback_data'=>'nolock'],['text'=>$_link,'callback_data'=>'lock_links']
],
[
  ['text'=>'🏷 التاك','callback_data'=>'nolock'],['text'=>$_tag,'callback_data'=>'lock_tag']
],
[
  ['text'=>'🏷 المعرف','callback_data'=>'nolock'],['text'=>$_username,'callback_data'=>'lock_username']
],
[
  ['text'=>'🏷 الارقام','callback_data'=>'nolock'],['text'=>$_num,'callback_data'=>'lock_number']
],
[
  ['text'=>'🏷 الويب','callback_data'=>'nolock'],['text'=>$_web,'callback_data'=>'lock_web']
],
[
  ['text'=>'🏷 الدردشه','callback_data'=>'nolock'],['text'=>"✅",'callback_data'=>'lock_chat']
],
[
  ['text'=>'🏷 التوجيه','callback_data'=>'nolock'],['text'=>$_fwd,'callback_data'=>'lock_fwd']
],
[
  ['text'=>'🏷 الرد','callback_data'=>'nolock'],['text'=>$_reply,'callback_data'=>'lock_reply']
],
[
  ['text'=>'🏷 التعديل','callback_data'=>'nolock'],['text'=>$_edit,'callback_data'=>'lock_edit']
],
[
  ['text'=>'🏷 الانجليزية','callback_data'=>'nolock'],['text'=>$_eng,'callback_data'=>'lock_eng']
],
[
  ['text'=>'🏷 العربية','callback_data'=>'nolock'],['text'=>$_arab,'callback_data'=>'lock_arab']
],
[
  ['text'=>'🏷 الانضمام','callback_data'=>'nolock'],['text'=>$_join,'callback_data'=>'lock_join']
],
[
  ['text'=>'🏷 البوتات','callback_data'=>'nolock'],['text'=>$_bot,'callback_data'=>'lock_bots']
],
	[
  ['text'=>'🏷 المغادرة','callback_data'=>'nolock'],['text'=>$_kickme,'callback_data'=>'lock_kickme']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_chat" && $_chat == "✅"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_settings == "❌"){
save("data/$chat_id2/settings/chat.txt","❌");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'🏷 التكرار','callback_data'=>'nolock'],['text'=>$_flood,'callback_data'=>'lock_flood']
],
[
  ['text'=>'🏷 الروابط','callback_data'=>'nolock'],['text'=>$_link,'callback_data'=>'lock_links']
],
[
  ['text'=>'🏷 التاك','callback_data'=>'nolock'],['text'=>$_tag,'callback_data'=>'lock_tag']
],
[
  ['text'=>'🏷 المعرف','callback_data'=>'nolock'],['text'=>$_username,'callback_data'=>'lock_username']
],
[
  ['text'=>'🏷 الارقام','callback_data'=>'nolock'],['text'=>$_num,'callback_data'=>'lock_number']
],
[
  ['text'=>'🏷 الويب','callback_data'=>'nolock'],['text'=>$_web,'callback_data'=>'lock_web']
],
[
  ['text'=>'🏷 الدردشه','callback_data'=>'nolock'],['text'=>"❌",'callback_data'=>'lock_chat']
],
[
  ['text'=>'🏷 التوجيه','callback_data'=>'nolock'],['text'=>$_fwd,'callback_data'=>'lock_fwd']
],
[
  ['text'=>'🏷 الرد','callback_data'=>'nolock'],['text'=>$_reply,'callback_data'=>'lock_reply']
],
[
  ['text'=>'🏷 التعديل','callback_data'=>'nolock'],['text'=>$_edit,'callback_data'=>'lock_edit']
],
[
  ['text'=>'🏷 الانجليزية','callback_data'=>'nolock'],['text'=>$_eng,'callback_data'=>'lock_eng']
],
[
  ['text'=>'🏷 العربية','callback_data'=>'nolock'],['text'=>$_arab,'callback_data'=>'lock_arab']
],
[
  ['text'=>'🏷 الانضمام','callback_data'=>'nolock'],['text'=>$_join,'callback_data'=>'lock_join']
],
[
  ['text'=>'🏷 البوتات','callback_data'=>'nolock'],['text'=>$_bot,'callback_data'=>'lock_bots']
],
	[
  ['text'=>'🏷 المغادرة','callback_data'=>'nolock'],['text'=>$_kickme,'callback_data'=>'lock_kickme']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_fwd" && $_fwd == "❌"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_settings == "❌"){
save("data/$chat_id2/settings/fwd.txt","✅");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'🏷 التكرار','callback_data'=>'nolock'],['text'=>$_flood,'callback_data'=>'lock_flood']
],
[
  ['text'=>'🏷 الروابط','callback_data'=>'nolock'],['text'=>$_link,'callback_data'=>'lock_links']
],
[
  ['text'=>'🏷 التاك','callback_data'=>'nolock'],['text'=>$_tag,'callback_data'=>'lock_tag']
],
[
  ['text'=>'🏷 المعرف','callback_data'=>'nolock'],['text'=>$_username,'callback_data'=>'lock_username']
],
[
  ['text'=>'🏷 الارقام','callback_data'=>'nolock'],['text'=>$_num,'callback_data'=>'lock_number']
],
[
  ['text'=>'🏷 الويب','callback_data'=>'nolock'],['text'=>$_web,'callback_data'=>'lock_web']
],
[
  ['text'=>'🏷 الدردشه','callback_data'=>'nolock'],['text'=>$_chat,'callback_data'=>'lock_chat']
],
[
  ['text'=>'🏷 التوجيه','callback_data'=>'nolock'],['text'=>"✅",'callback_data'=>'lock_fwd']
],
[
  ['text'=>'🏷 الرد','callback_data'=>'nolock'],['text'=>$_reply,'callback_data'=>'lock_reply']
],
[
  ['text'=>'🏷 التعديل','callback_data'=>'nolock'],['text'=>$_edit,'callback_data'=>'lock_edit']
],
[
  ['text'=>'🏷 الانجليزية','callback_data'=>'nolock'],['text'=>$_eng,'callback_data'=>'lock_eng']
],
[
  ['text'=>'🏷 العربية','callback_data'=>'nolock'],['text'=>$_arab,'callback_data'=>'lock_arab']
],
[
  ['text'=>'🏷 الانضمام','callback_data'=>'nolock'],['text'=>$_join,'callback_data'=>'lock_join']
],
[
  ['text'=>'🏷 البوتات','callback_data'=>'nolock'],['text'=>$_bot,'callback_data'=>'lock_bots']
],
	[
  ['text'=>'🏷 المغادرة','callback_data'=>'nolock'],['text'=>$_kickme,'callback_data'=>'lock_kickme']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_fwd" && $_fwd == "✅"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_settings == "❌"){
save("data/$chat_id2/settings/fwd.txt","❌");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'🏷 التكرار','callback_data'=>'nolock'],['text'=>$_flood,'callback_data'=>'lock_flood']
],
[
  ['text'=>'🏷 الروابط','callback_data'=>'nolock'],['text'=>$_link,'callback_data'=>'lock_links']
],
[
  ['text'=>'🏷 التاك','callback_data'=>'nolock'],['text'=>$_tag,'callback_data'=>'lock_tag']
],
[
  ['text'=>'🏷 المعرف','callback_data'=>'nolock'],['text'=>$_username,'callback_data'=>'lock_username']
],
[
  ['text'=>'🏷 الارقام','callback_data'=>'nolock'],['text'=>$_num,'callback_data'=>'lock_number']
],
[
  ['text'=>'🏷 الويب','callback_data'=>'nolock'],['text'=>$_web,'callback_data'=>'lock_web']
],
[
  ['text'=>'🏷 الدردشه','callback_data'=>'nolock'],['text'=>$_chat,'callback_data'=>'lock_chat']
],
[
  ['text'=>'🏷 التوجيه','callback_data'=>'nolock'],['text'=>"❌",'callback_data'=>'lock_fwd']
],
[
  ['text'=>'🏷 الرد','callback_data'=>'nolock'],['text'=>$_reply,'callback_data'=>'lock_reply']
],
[
  ['text'=>'🏷 التعديل','callback_data'=>'nolock'],['text'=>$_edit,'callback_data'=>'lock_edit']
],
[
  ['text'=>'🏷 الانجليزية','callback_data'=>'nolock'],['text'=>$_eng,'callback_data'=>'lock_eng']
],
[
  ['text'=>'🏷 العربية','callback_data'=>'nolock'],['text'=>$_arab,'callback_data'=>'lock_arab']
],
[
  ['text'=>'🏷 الانضمام','callback_data'=>'nolock'],['text'=>$_join,'callback_data'=>'lock_join']
],
[
  ['text'=>'🏷 البوتات','callback_data'=>'nolock'],['text'=>$_bot,'callback_data'=>'lock_bots']
],
	[
  ['text'=>'🏷 المغادرة','callback_data'=>'nolock'],['text'=>$_kickme,'callback_data'=>'lock_kickme']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_reply" && $_reply == "❌"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_settings == "❌"){
save("data/$chat_id2/settings/reply.txt","✅");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'🏷 التكرار','callback_data'=>'nolock'],['text'=>$_flood,'callback_data'=>'lock_flood']
],
[
  ['text'=>'🏷 الروابط','callback_data'=>'nolock'],['text'=>$_link,'callback_data'=>'lock_links']
],
[
  ['text'=>'🏷 التاك','callback_data'=>'nolock'],['text'=>$_tag,'callback_data'=>'lock_tag']
],
[
  ['text'=>'🏷 المعرف','callback_data'=>'nolock'],['text'=>$_username,'callback_data'=>'lock_username']
],
[
  ['text'=>'🏷 الارقام','callback_data'=>'nolock'],['text'=>$_num,'callback_data'=>'lock_number']
],
[
  ['text'=>'🏷 الويب','callback_data'=>'nolock'],['text'=>$_web,'callback_data'=>'lock_web']
],
[
  ['text'=>'🏷 الدردشه','callback_data'=>'nolock'],['text'=>$_chat,'callback_data'=>'lock_chat']
],
[
  ['text'=>'🏷 التوجيه','callback_data'=>'nolock'],['text'=>$_fwd,'callback_data'=>'lock_fwd']
],
[
  ['text'=>'🏷 الرد','callback_data'=>'nolock'],['text'=>"✅",'callback_data'=>'lock_reply']
],
[
  ['text'=>'🏷 التعديل','callback_data'=>'nolock'],['text'=>$_edit,'callback_data'=>'lock_edit']
],
[
  ['text'=>'🏷 الانجليزية','callback_data'=>'nolock'],['text'=>$_eng,'callback_data'=>'lock_eng']
],
[
  ['text'=>'🏷 العربية','callback_data'=>'nolock'],['text'=>$_arab,'callback_data'=>'lock_arab']
],
[
  ['text'=>'🏷 الانضمام','callback_data'=>'nolock'],['text'=>$_join,'callback_data'=>'lock_join']
],
[
  ['text'=>'🏷 البوتات','callback_data'=>'nolock'],['text'=>$_bot,'callback_data'=>'lock_bots']
],
	[
  ['text'=>'🏷 المغادرة','callback_data'=>'nolock'],['text'=>$_kickme,'callback_data'=>'lock_kickme']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_reply" && $_reply == "✅"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_settings == "❌"){
save("data/$chat_id2/settings/reply.txt","❌");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'🏷 التكرار','callback_data'=>'nolock'],['text'=>$_flood,'callback_data'=>'lock_flood']
],
[
  ['text'=>'🏷 الروابط','callback_data'=>'nolock'],['text'=>$_link,'callback_data'=>'lock_links']
],
[
  ['text'=>'🏷 التاك','callback_data'=>'nolock'],['text'=>$_tag,'callback_data'=>'lock_tag']
],
[
  ['text'=>'🏷 المعرف','callback_data'=>'nolock'],['text'=>$_username,'callback_data'=>'lock_username']
],
[
  ['text'=>'🏷 الارقام','callback_data'=>'nolock'],['text'=>$_num,'callback_data'=>'lock_number']
],
[
  ['text'=>'🏷 الويب','callback_data'=>'nolock'],['text'=>$_web,'callback_data'=>'lock_web']
],
[
  ['text'=>'🏷 الدردشه','callback_data'=>'nolock'],['text'=>$_chat,'callback_data'=>'lock_chat']
],
[
  ['text'=>'🏷 التوجيه','callback_data'=>'nolock'],['text'=>$_fwd,'callback_data'=>'lock_fwd']
],
[
  ['text'=>'🏷 الرد','callback_data'=>'nolock'],['text'=>"❌",'callback_data'=>'lock_reply']
],
[
  ['text'=>'🏷 التعديل','callback_data'=>'nolock'],['text'=>$_edit,'callback_data'=>'lock_edit']
],
[
  ['text'=>'🏷 الانجليزية','callback_data'=>'nolock'],['text'=>$_eng,'callback_data'=>'lock_eng']
],
[
  ['text'=>'🏷 العربية','callback_data'=>'nolock'],['text'=>$_arab,'callback_data'=>'lock_arab']
],
[
  ['text'=>'🏷 الانضمام','callback_data'=>'nolock'],['text'=>$_join,'callback_data'=>'lock_join']
],
[
  ['text'=>'🏷 البوتات','callback_data'=>'nolock'],['text'=>$_bot,'callback_data'=>'lock_bots']
],
	[
  ['text'=>'🏷 المغادرة','callback_data'=>'nolock'],['text'=>$_kickme,'callback_data'=>'lock_kickme']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}


   if($data == "lock_edit" && $_edit == "❌"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_settings == "❌"){
save("data/$chat_id2/settings/edit.txt","✅");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'🏷 التكرار','callback_data'=>'nolock'],['text'=>$_flood,'callback_data'=>'lock_flood']
],
[
  ['text'=>'🏷 الروابط','callback_data'=>'nolock'],['text'=>$_link,'callback_data'=>'lock_links']
],
[
  ['text'=>'🏷 التاك','callback_data'=>'nolock'],['text'=>$_tag,'callback_data'=>'lock_tag']
],
[
  ['text'=>'🏷 المعرف','callback_data'=>'nolock'],['text'=>$_username,'callback_data'=>'lock_username']
],
[
  ['text'=>'🏷 الارقام','callback_data'=>'nolock'],['text'=>$_num,'callback_data'=>'lock_number']
],
[
  ['text'=>'🏷 الويب','callback_data'=>'nolock'],['text'=>$_web,'callback_data'=>'lock_web']
],
[
  ['text'=>'🏷 الدردشه','callback_data'=>'nolock'],['text'=>$_chat,'callback_data'=>'lock_chat']
],
[
  ['text'=>'🏷 التوجيه','callback_data'=>'nolock'],['text'=>$_fwd,'callback_data'=>'lock_fwd']
],
[
  ['text'=>'🏷 الرد','callback_data'=>'nolock'],['text'=>$_reply,'callback_data'=>'lock_reply']
],
[
  ['text'=>'🏷 التعديل','callback_data'=>'nolock'],['text'=>"✅",'callback_data'=>'lock_edit']
],
[
  ['text'=>'🏷 الانجليزية','callback_data'=>'nolock'],['text'=>$_eng,'callback_data'=>'lock_eng']
],
[
  ['text'=>'🏷 العربية','callback_data'=>'nolock'],['text'=>$_arab,'callback_data'=>'lock_arab']
],
[
  ['text'=>'🏷 الانضمام','callback_data'=>'nolock'],['text'=>$_join,'callback_data'=>'lock_join']
],
[
  ['text'=>'🏷 البوتات','callback_data'=>'nolock'],['text'=>$_bot,'callback_data'=>'lock_bots']
],
	[
  ['text'=>'🏷 المغادرة','callback_data'=>'nolock'],['text'=>$_kickme,'callback_data'=>'lock_kickme']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_edit" && $_edit == "✅"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_settings == "❌"){
save("data/$chat_id2/settings/edit.txt","❌");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'🏷 التكرار','callback_data'=>'nolock'],['text'=>$_flood,'callback_data'=>'lock_flood']
],
[
  ['text'=>'🏷 الروابط','callback_data'=>'nolock'],['text'=>$_link,'callback_data'=>'lock_links']
],
[
  ['text'=>'🏷 التاك','callback_data'=>'nolock'],['text'=>$_tag,'callback_data'=>'lock_tag']
],
[
  ['text'=>'🏷 المعرف','callback_data'=>'nolock'],['text'=>$_username,'callback_data'=>'lock_username']
],
[
  ['text'=>'🏷 الارقام','callback_data'=>'nolock'],['text'=>$_num,'callback_data'=>'lock_number']
],
[
  ['text'=>'🏷 الويب','callback_data'=>'nolock'],['text'=>$_web,'callback_data'=>'lock_web']
],
[
  ['text'=>'🏷 الدردشه','callback_data'=>'nolock'],['text'=>$_chat,'callback_data'=>'lock_chat']
],
[
  ['text'=>'🏷 التوجيه','callback_data'=>'nolock'],['text'=>$_fwd,'callback_data'=>'lock_fwd']
],
[
  ['text'=>'🏷 الرد','callback_data'=>'nolock'],['text'=>$_reply,'callback_data'=>'lock_reply']
],
[
  ['text'=>'🏷 التعديل','callback_data'=>'nolock'],['text'=>"❌",'callback_data'=>'lock_edit']
],
[
  ['text'=>'🏷 الانجليزية','callback_data'=>'nolock'],['text'=>$_eng,'callback_data'=>'lock_eng']
],
[
  ['text'=>'🏷 العربية','callback_data'=>'nolock'],['text'=>$_arab,'callback_data'=>'lock_arab']
],
[
  ['text'=>'🏷 الانضمام','callback_data'=>'nolock'],['text'=>$_join,'callback_data'=>'lock_join']
],
[
  ['text'=>'🏷 البوتات','callback_data'=>'nolock'],['text'=>$_bot,'callback_data'=>'lock_bots']
],
	[
  ['text'=>'🏷 المغادرة','callback_data'=>'nolock'],['text'=>$_kickme,'callback_data'=>'lock_kickme']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}


   if($data == "lock_eng" && $_eng == "❌"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_settings == "❌"){
save("data/$chat_id2/settings/eng.txt","✅");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'🏷 التكرار','callback_data'=>'nolock'],['text'=>$_flood,'callback_data'=>'lock_flood']
],
[
  ['text'=>'🏷 الروابط','callback_data'=>'nolock'],['text'=>$_link,'callback_data'=>'lock_links']
],
[
  ['text'=>'🏷 التاك','callback_data'=>'nolock'],['text'=>$_tag,'callback_data'=>'lock_tag']
],
[
  ['text'=>'🏷 المعرف','callback_data'=>'nolock'],['text'=>$_username,'callback_data'=>'lock_username']
],
[
  ['text'=>'🏷 الارقام','callback_data'=>'nolock'],['text'=>$_num,'callback_data'=>'lock_number']
],
[
  ['text'=>'🏷 الويب','callback_data'=>'nolock'],['text'=>$_web,'callback_data'=>'lock_web']
],
[
  ['text'=>'🏷 الدردشه','callback_data'=>'nolock'],['text'=>$_chat,'callback_data'=>'lock_chat']
],
[
  ['text'=>'🏷 التوجيه','callback_data'=>'nolock'],['text'=>$_fwd,'callback_data'=>'lock_fwd']
],
[
  ['text'=>'🏷 الرد','callback_data'=>'nolock'],['text'=>$_reply,'callback_data'=>'lock_reply']
],
[
  ['text'=>'🏷 التعديل','callback_data'=>'nolock'],['text'=>$_edit,'callback_data'=>'lock_edit']
],
[
  ['text'=>'🏷 الانجليزية','callback_data'=>'nolock'],['text'=>"✅",'callback_data'=>'lock_eng']
],
[
  ['text'=>'🏷 العربية','callback_data'=>'nolock'],['text'=>$_arab,'callback_data'=>'lock_arab']
],
[
  ['text'=>'🏷 الانضمام','callback_data'=>'nolock'],['text'=>$_join,'callback_data'=>'lock_join']
],
[
  ['text'=>'🏷 البوتات','callback_data'=>'nolock'],['text'=>$_bot,'callback_data'=>'lock_bots']
],
	[
  ['text'=>'🏷 المغادرة','callback_data'=>'nolock'],['text'=>$_kickme,'callback_data'=>'lock_kickme']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_eng" && $_eng == "✅"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_settings == "❌"){
save("data/$chat_id2/settings/eng.txt","❌");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'🏷 التكرار','callback_data'=>'nolock'],['text'=>$_flood,'callback_data'=>'lock_flood']
],
[
  ['text'=>'🏷 الروابط','callback_data'=>'nolock'],['text'=>$_link,'callback_data'=>'lock_links']
],
[
  ['text'=>'🏷 التاك','callback_data'=>'nolock'],['text'=>$_tag,'callback_data'=>'lock_tag']
],
[
  ['text'=>'🏷 المعرف','callback_data'=>'nolock'],['text'=>$_username,'callback_data'=>'lock_username']
],
[
  ['text'=>'🏷 الارقام','callback_data'=>'nolock'],['text'=>$_num,'callback_data'=>'lock_number']
],
[
  ['text'=>'🏷 الويب','callback_data'=>'nolock'],['text'=>$_web,'callback_data'=>'lock_web']
],
[
  ['text'=>'🏷 الدردشة','callback_data'=>'nolock'],['text'=>$_chat,'callback_data'=>'lock_chat']
],
[
  ['text'=>'🏷 التوجيه','callback_data'=>'nolock'],['text'=>$_fwd,'callback_data'=>'lock_fwd']
],
[
  ['text'=>'🏷 الرد','callback_data'=>'nolock'],['text'=>$_reply,'callback_data'=>'lock_reply']
],
[
  ['text'=>'🏷 التعديل','callback_data'=>'nolock'],['text'=>$_edit,'callback_data'=>'lock_edit']
],
[
  ['text'=>'🏷 الانجليزية','callback_data'=>'nolock'],['text'=>"❌",'callback_data'=>'lock_eng']
],
[
  ['text'=>'🏷 العربية','callback_data'=>'nolock'],['text'=>$_arab,'callback_data'=>'lock_arab']
],
[
  ['text'=>'🏷 الانضمام','callback_data'=>'nolock'],['text'=>$_join,'callback_data'=>'lock_join']
],
[
  ['text'=>'🏷 البوتات','callback_data'=>'nolock'],['text'=>$_bot,'callback_data'=>'lock_bots']
],
	[
  ['text'=>'🏷 المغادرة','callback_data'=>'nolock'],['text'=>$_kickme,'callback_data'=>'lock_kickme']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_arab" && $_arab == "❌"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_settings == "❌"){
save("data/$chat_id2/settings/arab.txt","✅");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'🏷 التكرار','callback_data'=>'nolock'],['text'=>$_flood,'callback_data'=>'lock_flood']
],
[
  ['text'=>'🏷 الروابط','callback_data'=>'nolock'],['text'=>$_link,'callback_data'=>'lock_links']
],
[
  ['text'=>'🏷 التاك','callback_data'=>'nolock'],['text'=>$_tag,'callback_data'=>'lock_tag']
],
[
  ['text'=>'🏷 المعرف','callback_data'=>'nolock'],['text'=>$_username,'callback_data'=>'lock_username']
],
[
  ['text'=>'🏷 الارقام','callback_data'=>'nolock'],['text'=>$_num,'callback_data'=>'lock_number']
],
[
  ['text'=>'🏷 الويب','callback_data'=>'nolock'],['text'=>$_web,'callback_data'=>'lock_web']
],
[
  ['text'=>'🏷 الدردشة','callback_data'=>'nolock'],['text'=>$_chat,'callback_data'=>'lock_chat']
],
[
  ['text'=>'🏷 التوجيه','callback_data'=>'nolock'],['text'=>$_fwd,'callback_data'=>'lock_fwd']
],
[
  ['text'=>'🏷 الرد','callback_data'=>'nolock'],['text'=>$_reply,'callback_data'=>'lock_reply']
],
[
  ['text'=>'🏷 التعديل','callback_data'=>'nolock'],['text'=>$_edit,'callback_data'=>'lock_edit']
],
[
  ['text'=>'🏷 الانجليزية','callback_data'=>'nolock'],['text'=>$_eng,'callback_data'=>'lock_eng']
],
[
  ['text'=>'🏷 العربية','callback_data'=>'nolock'],['text'=>"✅",'callback_data'=>'lock_arab']
],
[
  ['text'=>'🏷 الانضمام','callback_data'=>'nolock'],['text'=>$_join,'callback_data'=>'lock_join']
],
[
  ['text'=>'🏷 البوتات','callback_data'=>'nolock'],['text'=>$_bot,'callback_data'=>'lock_bots']
],
	[
  ['text'=>'🏷 المغادرة','callback_data'=>'nolock'],['text'=>$_kickme,'callback_data'=>'lock_kickme']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_arab" && $_arab == "✅"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_settings == "❌"){
save("data/$chat_id2/settings/arab.txt","❌");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'🏷 التكرار','callback_data'=>'nolock'],['text'=>$_flood,'callback_data'=>'lock_flood']
],
[
  ['text'=>'🏷 الروابط','callback_data'=>'nolock'],['text'=>$_link,'callback_data'=>'lock_links']
],
[
  ['text'=>'🏷 التاك','callback_data'=>'nolock'],['text'=>$_tag,'callback_data'=>'lock_tag']
],
[
  ['text'=>'🏷 المعرف','callback_data'=>'nolock'],['text'=>$_username,'callback_data'=>'lock_username']
],
[
  ['text'=>'🏷 الارقام','callback_data'=>'nolock'],['text'=>$_num,'callback_data'=>'lock_number']
],
[
  ['text'=>'🏷 الويب','callback_data'=>'nolock'],['text'=>$_web,'callback_data'=>'lock_web']
],
[
  ['text'=>'🏷 الدردشة','callback_data'=>'nolock'],['text'=>$_chat,'callback_data'=>'lock_chat']
],
[
  ['text'=>'🏷 التوجيه','callback_data'=>'nolock'],['text'=>$_fwd,'callback_data'=>'lock_fwd']
],
[
  ['text'=>'🏷 الرد','callback_data'=>'nolock'],['text'=>$_reply,'callback_data'=>'lock_reply']
],
[
  ['text'=>'🏷 التعديل','callback_data'=>'nolock'],['text'=>$_edit,'callback_data'=>'lock_edit']
],
[
  ['text'=>'🏷 الانجليزية','callback_data'=>'nolock'],['text'=>$_eng,'callback_data'=>'lock_eng']
],
[
  ['text'=>'🏷 العربية','callback_data'=>'nolock'],['text'=>"❌",'callback_data'=>'lock_arab']
],
[
  ['text'=>'🏷 الانضمام','callback_data'=>'nolock'],['text'=>$_join,'callback_data'=>'lock_join']
],
[
  ['text'=>'🏷 البوتات','callback_data'=>'nolock'],['text'=>$_bot,'callback_data'=>'lock_bots']
],
	[
  ['text'=>'🏷 المغادرة','callback_data'=>'nolock'],['text'=>$_kickme,'callback_data'=>'lock_kickme']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}


   if($data == "lock_join" && $_join == "❌"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_settings == "❌"){
save("data/$chat_id2/settings/join.txt","✅");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'🏷 التكرار','callback_data'=>'nolock'],['text'=>$_flood,'callback_data'=>'lock_flood']
],
[
  ['text'=>'🏷 الروابط','callback_data'=>'nolock'],['text'=>$_link,'callback_data'=>'lock_links']
],
[
  ['text'=>'🏷 التاك','callback_data'=>'nolock'],['text'=>$_tag,'callback_data'=>'lock_tag']
],
[
  ['text'=>'🏷 المعرف','callback_data'=>'nolock'],['text'=>$_username,'callback_data'=>'lock_username']
],
[
  ['text'=>'🏷 الارقام','callback_data'=>'nolock'],['text'=>$_num,'callback_data'=>'lock_number']
],
[
  ['text'=>'🏷 الويب','callback_data'=>'nolock'],['text'=>$_web,'callback_data'=>'lock_web']
],
[
  ['text'=>'🏷 الدردشة','callback_data'=>'nolock'],['text'=>$_chat,'callback_data'=>'lock_chat']
],
[
  ['text'=>'🏷 التوجيه','callback_data'=>'nolock'],['text'=>$_fwd,'callback_data'=>'lock_fwd']
],
[
  ['text'=>'🏷 الرد','callback_data'=>'nolock'],['text'=>$_reply,'callback_data'=>'lock_reply']
],
[
  ['text'=>'🏷 التعديل','callback_data'=>'nolock'],['text'=>$_edit,'callback_data'=>'lock_edit']
],
[
  ['text'=>'🏷 الانجليزية','callback_data'=>'nolock'],['text'=>$_eng,'callback_data'=>'lock_eng']
],
[
  ['text'=>'🏷 العربية','callback_data'=>'nolock'],['text'=>$_arab,'callback_data'=>'lock_arab']
],
[
  ['text'=>'🏷 الانضمام','callback_data'=>'nolock'],['text'=>"✅",'callback_data'=>'lock_join']
],
	[
  ['text'=>'🏷 المغادرة','callback_data'=>'nolock'],['text'=>$_kickme,'callback_data'=>'lock_kickme']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_join" && $_join == "✅"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_settings == "❌"){
save("data/$chat_id2/settings/join.txt","❌");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'🏷 التكرار','callback_data'=>'nolock'],['text'=>$_flood,'callback_data'=>'lock_flood']
],
[
  ['text'=>'🏷 الروابط','callback_data'=>'nolock'],['text'=>$_link,'callback_data'=>'lock_links']
],
[
  ['text'=>'🏷 التاك','callback_data'=>'nolock'],['text'=>$_tag,'callback_data'=>'lock_tag']
],
[
  ['text'=>'🏷 المعرف','callback_data'=>'nolock'],['text'=>$_username,'callback_data'=>'lock_username']
],
[
  ['text'=>'🏷 الارقام','callback_data'=>'nolock'],['text'=>$_num,'callback_data'=>'lock_number']
],
[
  ['text'=>'🏷 الويب','callback_data'=>'nolock'],['text'=>$_web,'callback_data'=>'lock_web']
],
[
  ['text'=>'🏷 الدردشة','callback_data'=>'nolock'],['text'=>$_chat,'callback_data'=>'lock_chat']
],
[
  ['text'=>'🏷 التوجيه','callback_data'=>'nolock'],['text'=>$_fwd,'callback_data'=>'lock_fwd']
],
[
  ['text'=>'🏷 الرد','callback_data'=>'nolock'],['text'=>$_reply,'callback_data'=>'lock_reply']
],
[
  ['text'=>'🏷 التعديل','callback_data'=>'nolock'],['text'=>$_edit,'callback_data'=>'lock_edit']
],
[
  ['text'=>'🏷 الانجليزية','callback_data'=>'nolock'],['text'=>$_eng,'callback_data'=>'lock_eng']
],
[
  ['text'=>'🏷 العربية','callback_data'=>'nolock'],['text'=>$_arab,'callback_data'=>'lock_arab']
],
[
  ['text'=>'🏷 الانضمام','callback_data'=>'nolock'],['text'=>"❌",'callback_data'=>'lock_join']
],
	[
  ['text'=>'🏷 المغادرة','callback_data'=>'nolock'],['text'=>$_kickme,'callback_data'=>'lock_kickme']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}


   if($data == "lock_kickme" && $_kickme == "❌"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_settings == "❌"){
save("data/$chat_id2/settings/kickme.txt","✅");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'🏷 التكرار','callback_data'=>'nolock'],['text'=>$_flood,'callback_data'=>'lock_flood']
],
[
  ['text'=>'🏷 الروابط','callback_data'=>'nolock'],['text'=>$_link,'callback_data'=>'lock_links']
],
[
  ['text'=>'🏷 التاك','callback_data'=>'nolock'],['text'=>$_tag,'callback_data'=>'lock_tag']
],
[
  ['text'=>'🏷 المعرف','callback_data'=>'nolock'],['text'=>$_username,'callback_data'=>'lock_username']
],
[
  ['text'=>'🏷 الارقام','callback_data'=>'nolock'],['text'=>$_num,'callback_data'=>'lock_number']
],
[
  ['text'=>'🏷 الويب','callback_data'=>'nolock'],['text'=>$_web,'callback_data'=>'lock_web']
],
[
  ['text'=>'🏷 الدردشة','callback_data'=>'nolock'],['text'=>$_chat,'callback_data'=>'lock_chat']
],
[
  ['text'=>'🏷 التوجيه','callback_data'=>'nolock'],['text'=>$_fwd,'callback_data'=>'lock_fwd']
],
[
  ['text'=>'🏷 الرد','callback_data'=>'nolock'],['text'=>$_reply,'callback_data'=>'lock_reply']
],
[
  ['text'=>'🏷 التعديل','callback_data'=>'nolock'],['text'=>$_edit,'callback_data'=>'lock_edit']
],
[
  ['text'=>'🏷 الانجليزية','callback_data'=>'nolock'],['text'=>$_eng,'callback_data'=>'lock_eng']
],
[
  ['text'=>'🏷 العربية','callback_data'=>'nolock'],['text'=>$_arab,'callback_data'=>'lock_arab']
],
[
  ['text'=>'🏷 الانضمام','callback_data'=>'nolock'],['text'=>$_join,'callback_data'=>'lock_join']
],
[
  ['text'=>'🏷 البوتات','callback_data'=>'nolock'],['text'=>$_bot,'callback_data'=>'lock_bots']
],
	[
  ['text'=>'🏷 المغادرة','callback_data'=>'nolock'],['text'=>"✅",'callback_data'=>'lock_kickme']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_kickme" && $_kickme == "✅"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_settings == "❌"){
save("data/$chat_id2/settings/kickme.txt","❌");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'🏷 التكرار','callback_data'=>'nolock'],['text'=>$_flood,'callback_data'=>'lock_flood']
],
[
  ['text'=>'🏷 الروابط','callback_data'=>'nolock'],['text'=>$_link,'callback_data'=>'lock_links']
],
[
  ['text'=>'🏷 التاك','callback_data'=>'nolock'],['text'=>$_tag,'callback_data'=>'lock_tag']
],
[
  ['text'=>'🏷 المعرف','callback_data'=>'nolock'],['text'=>$_username,'callback_data'=>'lock_username']
],
[
  ['text'=>'🏷 الارقام','callback_data'=>'nolock'],['text'=>$_num,'callback_data'=>'lock_number']
],
[
  ['text'=>'🏷 الويب','callback_data'=>'nolock'],['text'=>$_web,'callback_data'=>'lock_web']
],
[
  ['text'=>'🏷 الدردشة','callback_data'=>'nolock'],['text'=>$_chat,'callback_data'=>'lock_chat']
],
[
  ['text'=>'🏷 التوجيه','callback_data'=>'nolock'],['text'=>$_fwd,'callback_data'=>'lock_fwd']
],
[
  ['text'=>'🏷 الرد','callback_data'=>'nolock'],['text'=>$_reply,'callback_data'=>'lock_reply']
],
[
  ['text'=>'🏷 التعديل','callback_data'=>'nolock'],['text'=>$_edit,'callback_data'=>'lock_edit']
],
[
  ['text'=>'🏷 الانجليزية','callback_data'=>'nolock'],['text'=>$_eng,'callback_data'=>'lock_eng']
],
[
  ['text'=>'🏷 العربية','callback_data'=>'nolock'],['text'=>$_arab,'callback_data'=>'lock_arab']
],
[
  ['text'=>'🏷 الانضمام','callback_data'=>'nolock'],['text'=>$_join,'callback_data'=>'lock_join']
],
[
  ['text'=>'🏷 البوتات','callback_data'=>'nolock'],['text'=>$_bot,'callback_data'=>'lock_bots']
],
	[
  ['text'=>'🏷 المغادرة','callback_data'=>'nolock'],['text'=>"❌",'callback_data'=>'lock_kickme']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"قفل اخراج غیر فعال شد ❌",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_bots" && $_bot == "❌"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_settings == "❌"){
save("data/$chat_id2/settings/bot.txt","✅");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'🏷 التكرار','callback_data'=>'nolock'],['text'=>$_flood,'callback_data'=>'lock_flood']
],
[
  ['text'=>'🏷 الروابط','callback_data'=>'nolock'],['text'=>$_link,'callback_data'=>'lock_links']
],
[
  ['text'=>'🏷 التاك','callback_data'=>'nolock'],['text'=>$_tag,'callback_data'=>'lock_tag']
],
[
  ['text'=>'🏷 المعرف','callback_data'=>'nolock'],['text'=>$_username,'callback_data'=>'lock_username']
],
[
  ['text'=>'🏷 الارقام','callback_data'=>'nolock'],['text'=>$_num,'callback_data'=>'lock_number']
],
[
  ['text'=>'🏷 الويب','callback_data'=>'nolock'],['text'=>$_web,'callback_data'=>'lock_web']
],
[
  ['text'=>'🏷 الدردشة','callback_data'=>'nolock'],['text'=>$_chat,'callback_data'=>'lock_chat']
],
[
  ['text'=>'🏷 التوجيه','callback_data'=>'nolock'],['text'=>$_fwd,'callback_data'=>'lock_fwd']
],
[
  ['text'=>'🏷 الرد','callback_data'=>'nolock'],['text'=>$_reply,'callback_data'=>'lock_reply']
],
[
  ['text'=>'🏷 التعديل','callback_data'=>'nolock'],['text'=>$_edit,'callback_data'=>'lock_edit']
],
[
  ['text'=>'🏷 الانجليزية','callback_data'=>'nolock'],['text'=>$_eng,'callback_data'=>'lock_eng']
],
[
  ['text'=>'🏷 العربية','callback_data'=>'nolock'],['text'=>$_arab,'callback_data'=>'lock_arab']
],
[
  ['text'=>'🏷 الانضمام','callback_data'=>'nolock'],['text'=>$_join,'callback_data'=>'lock_join']
],
[
  ['text'=>'🏷 البوتات','callback_data'=>'nolock'],['text'=>"✅",'callback_data'=>'lock_bots']
],
	[
  ['text'=>'🏷 المغادرة','callback_data'=>'nolock'],['text'=>$_kickme,'callback_data'=>'lock_kickme']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_bots" && $_bot == "✅"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_settings == "❌"){
save("data/$chat_id2/settings/bot.txt","❌");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'🏷 التكرار','callback_data'=>'nolock'],['text'=>$_flood,'callback_data'=>'lock_flood']
],
[
  ['text'=>'🏷 الروابط','callback_data'=>'nolock'],['text'=>$_link,'callback_data'=>'lock_links']
],
[
  ['text'=>'🏷 التاك','callback_data'=>'nolock'],['text'=>$_tag,'callback_data'=>'lock_tag']
],
[
  ['text'=>'🏷 المعرف','callback_data'=>'nolock'],['text'=>$_username,'callback_data'=>'lock_username']
],
[
  ['text'=>'🏷 الارقام','callback_data'=>'nolock'],['text'=>$_num,'callback_data'=>'lock_number']
],
[
  ['text'=>'🏷 الويب','callback_data'=>'nolock'],['text'=>$_web,'callback_data'=>'lock_web']
],
[
  ['text'=>'🏷 الدردشة','callback_data'=>'nolock'],['text'=>$_chat,'callback_data'=>'lock_chat']
],
[
  ['text'=>'🏷 التوجيه','callback_data'=>'nolock'],['text'=>$_fwd,'callback_data'=>'lock_fwd']
],
[
  ['text'=>'🏷 الرد','callback_data'=>'nolock'],['text'=>$_reply,'callback_data'=>'lock_reply']
],
[
  ['text'=>'🏷 التعديل','callback_data'=>'nolock'],['text'=>$_edit,'callback_data'=>'lock_edit']
],
[
  ['text'=>'🏷 الانجليزية','callback_data'=>'nolock'],['text'=>$_eng,'callback_data'=>'lock_eng']
],
[
  ['text'=>'🏷 العربية','callback_data'=>'nolock'],['text'=>$_arab,'callback_data'=>'lock_arab']
],
[
  ['text'=>'🏷 الانضمام','callback_data'=>'nolock'],['text'=>$_join,'callback_data'=>'lock_join']
],
[
  ['text'=>'🏷 البوتات','callback_data'=>'nolock'],['text'=>"❌",'callback_data'=>'lock_bots']
],
	[
  ['text'=>'🏷 المغادرة','callback_data'=>'nolock'],['text'=>$_kickme,'callback_data'=>'lock_kickme']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •لقائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}
//----------lock and unlock by text----------\\
if ($textmessage == 'قفل الروابط' || $textmessage == '/lock links' || $textmessage == 'قفل روابط') {
	if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_settings2 == "❌"){
save("data/$chat_id/settings/link.txt","✅");
makereq('sendMessage',[
'chat_id'=> $update->message->chat->id,
'text' => '- اهلا عزيزي تم قفل 🏴 الروابط في المجموعةه بنجاح ☑️ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 🔖](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			 );
}
}

	if ($textmessage == 'فتح الروابط' || $textmessage == '/unlock links'  || $textmessage == 'فتح روابط' ) {
		if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_settings2 == "❌"){
		save("data/$chat_id/settings/link.txt","❌");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم فتح 🏳 الروابط في المجموعةه بنجاح ✅ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 📢](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
}
if ($textmessage == 'قفل الاشعارات' || $textmessage == '/lock join' || $textmessage == '#lock join') {
	if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_settings2 == "❌"){
save("data/$chat_id/settings/join.txt","✅");
makereq('sendMessage',[
'chat_id'=> $update->message->chat->id,
'text' => '- اهلا عزيزي تم قفل 🏴 الاشعارات في المجموعةه بنجاح ☑️ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 🔖](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			 );
}
}

	if ($textmessage == 'فتح الاشعارات' || $textmessage == 'فتح شعارات' || $textmessage == '/unlock join') {
		if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_settings2 == "❌"){
		save("data/$chat_id/settings/join.txt","❌");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم فتح 🏳 الاشعارات في المجموعةه بنجاح ✅ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 📢](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
}
if ($textmessage == 'قفل الدردشه' || $textmessage == '/lock chat' || $textmessage == '#lock chat') {
	if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_settings2 == "❌"){
save("data/$chat_id/settings/chat.txt","✅");
makereq('sendMessage',[
'chat_id'=> $update->message->chat->id,
'text' => '- اهلا عزيزي تم قفل 🏴 الدردشه في المجموعةه بنجاح ☑️ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 🔖](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]);
}
}
	if ($textmessage == 'فتح الدردشه' || $textmessage == '!unlock chat' || $textmessage == '#unlock chat') {
		if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_settings2 == "❌"){
		save("data/$chat_id/settings/chat.txt","❌");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم فتح 🏳 الدردشه في المجموعةه بنجاح ✅ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 📢](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
	}
if ($textmessage == 'قفل الويب' || $textmessage == '/lock web' || $textmessage == '#lock web') {
	if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_settings2 == "❌"){
save("data/$chat_id/settings/web.txt","✅");
makereq('sendMessage',[
'chat_id'=> $update->message->chat->id,
'text' => '- اهلا عزيزي تم قفل 🏴 الويب في المجموعةه بنجاح ☑️ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 🔖](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			 );
		
	}
}

	if ($textmessage == 'فتح الويب' || $textmessage == '/unlock web' || $textmessage == '#unlock web') {
		if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_settings2 == "❌"){
		save("data/$chat_id/settings/web.txt","❌");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم فتح 🏳 الويب في المجموعةه بنجاح ✅ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 📢](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
}
if ($textmessage == 'قفل الارقام' || $textmessage == '/lock number' || $textmessage == '#lock number') {
	if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_settings2 == "❌"){
save("data/$chat_id/settings/num.txt","✅");
makereq('sendMessage',[
'chat_id'=> $update->message->chat->id,
'text' => '- اهلا عزيزي تم قفل 🏴 الارقام في المجموعةه بنجاح ☑️ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 🔖](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]);
}
}
	if ($textmessage == 'فتح الارقام' || $textmessage == '/unlock number' || $textmessage == '#unlock number' ) {
		if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_settings2 == "❌"){
		save("data/$chat_id/settings/num.txt","❌");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم قفل 🏴 الارقام في المجموعةه بنجاح ☑️ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 🔖](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
}
if ($textmessage == 'قفل التاك' || $textmessage == '/lock tag' || $textmessage == '#lock tag') {
	if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_settings2 == "❌"){
save("data/$chat_id/settings/tag.txt","✅");
makereq('sendMessage',[
'chat_id'=> $update->message->chat->id,
'text' => '- اهلا عزيزي تم قفل 🏴 التاك في المجموعةه بنجاح ☑️ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 🔖](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]);
}
}
	if ($textmessage == 'فتح التاك' || $textmessage == '/unlock tag' || $textmessage == '#unlock tag') {
		if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_settings2 == "❌"){
		save("data/$chat_id/settings/tag.txt","❌");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم فتح 🏳 التاك في المجموعةه بنجاح ✅ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 📢](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
}
if ($textmessage == 'قفل المعرف' || $textmessage == '/lock username' || $textmessage == '#lock username') {
	if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_settings2 == "❌"){
save("data/$chat_id/settings/username.txt","✅");
makereq('sendMessage',[
'chat_id'=> $update->message->chat->id,
'text' => '- اهلا عزيزي تم قفل 🏴 اليوز في المجموعةه بنجاح ☑️ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 🔖](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]);
}
}
	if ($textmessage == 'فتح المعرف' || $textmessage == '/unlock username' || $textmessage == '#unlock username') {
		if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_settings2 == "❌"){
		save("data/$chat_id/settings/username.txt","❌");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم فتح 🏳 اليوزر في المجموعةه بنجاح ✅ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 📢](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
	}

	if ($textmessage == 'قفل التكرار' || $textmessage == '/lock flood' || $textmessage == '#lock flood') {
		if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_settings2 == "❌"){
		save("data/$chat_id/settings/flood.txt","✅");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم قفل 🏴 التكرار في المجموعةه بنجاح ☑️ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 🔖](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
	'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
}
	if ($textmessage == 'فتح التكرار' || $textmessage == '/unlock flood' || $textmessage == '#unlock flood') {
		if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_settings2 == "❌"){
		save("data/$chat_id/settings/flood.txt","❌");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم فتح 🏳 التكرار في المجموعةه بنجاح ✅ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 📢](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
	'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
}
if ($textmessage == 'قفل التوجيه' || $textmessage == '/lock forward' || $textmessage == '#lock forward') {
		if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_settings2 == "❌"){
save("data/$chat_id/settings/fwd.txt","✅");
makereq('sendMessage',[
'chat_id'=> $update->message->chat->id,
'text' => '- اهلا عزيزي تم قفل 🏴 التوجيه في المجموعةه بنجاح ☑️ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 🔖](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]);
}
}
	if ($textmessage == 'فتح التوجيه' || $textmessage == '/unlock forward' || $textmessage == '#unlock forward') {
		if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_settings2 == "❌"){
		save("data/$chat_id/settings/fwd.txt","❌");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم فتح 🏳 التوجيه في المجموعةه بنجاح ✅ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 📢](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
}
if ($textmessage == 'قفل الرد' || $textmessage == '/lock reply' || $textmessage == '#lock reply') {
	if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_settings2 == "❌"){
save("data/$chat_id/settings/reply.txt","✅");
makereq('sendMessage',[
'chat_id'=> $update->message->chat->id,
'text' => '- اهلا عزيزي تم قفل 🏴 الرد في المجموعةه بنجاح ☑️ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 🔖](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]);
}
}
	if ($textmessage == 'فتح الرد' || $textmessage == '/unlock reply' || $textmessage == '#unlock reply') {
		if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_settings2 == "❌"){
		save("data/$chat_id/settings/reply.txt","❌");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم فتح 🏳 الرد في المجموعةه بنجاح ✅ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 📢](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
	}
if ($textmessage == 'قفل التعديل' || $textmessage == '/lock edit' || $textmessage == '#lock edit') {
	if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_settings2 == "❌"){
save("data/$chat_id/settings/edit.txt","✅");
makereq('sendMessage',[
'chat_id'=> $update->message->chat->id,
'text' => '- اهلا عزيزي تم قفل 🏴 التعديل في المجموعةه بنجاح ☑️ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 🔖](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]);
}
}
	if ($textmessage == 'فتح التعديل' || $textmessage == '/unlock edit' || $textmessage == '#unlock edit') {
		if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_settings2 == "❌"){
		save("data/$chat_id/settings/edit.txt","❌");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم فتح 🏳 التعديل في المجموعةه بنجاح ✅ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 📢](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
	}
if ($textmessage == 'قفل الانجليزيه' || $textmessage == '/lock english'  || $textmessage == '#lock english' ) {
		if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_settings2 == "❌"){
save("data/$chat_id/settings/eng.txt","✅");
makereq('sendMessage',[
'chat_id'=> $update->message->chat->id,
'text' => '- اهلا عزيزي تم قفل 🏴 الانجليزيه في المجموعةه بنجاح ☑️ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 🔖](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]);
}
}
	if ($textmessage == 'فتح الانجليزيه' || $textmessage == '!unlock english' || $textmessage == '#unlock english') {
			if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_settings2 == "❌"){
		save("data/$chat_id/settings/eng.txt","❌");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم فتح 🏳 الانجليزيه في المجموعةه بنجاح ✅ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 📢](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
}
if ($textmessage == 'قفل المغادرة' || $textmessage == '/lock kickme' || $textmessage == '#lock kickme') {
	if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_settings2 == "❌"){
save("data/$chat_id/settings/kickme.txt","✅");
makereq('sendMessage',[
'chat_id'=> $update->message->chat->id,
'text' => '- اهلا عزيزي تم قفل 🏴 امر المغادرة في المجموعةه بنجاح ☑️ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 🔖](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]);
}
}
	if ($textmessage == 'فتح المغادرة' || $textmessage == '/unlock kickme' || $textmessage == '#unlock kickme') {
		if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_settings2 == "❌"){
		save("data/$chat_id/settings/kickme.txt","❌");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم فتح 🏳 امر المغادرة في المجموعةه بنجاح ✅ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 📢](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
	}
	if ($textmessage == 'قفل العربيه' || $textmessage == '/lock arabic' || $textmessage == '#lock arabic') {
			if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_settings2 == "❌"){
		save("data/$chat_id/settings/arab.txt","✅");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم قفل 🏴 العربيه في المجموعةه بنجاح ☑️ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 🔖](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
	'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
}
	if ($textmessage == 'فتح العربيه' || $textmessage == '!unlock arabic' || $textmessage == '#unlock arabic') {
	if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_settings2 == "❌"){
		save("data/$chat_id/settings/arab.txt","❌");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم فتح 🏳 العربيه في المجموعةه بنجاح ✅ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 📢](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
	'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
}
//-------End Lock and Unlock-------\\
//-------Start Mute and Unmute bu button-------\\
   if($data == "lock_sticker" && $_sticker == "❌"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_media == "❌"){
save("data/$chat_id2/settings/sticker.txt","✅");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'⚡️ الملصقات','callback_data'=>'nolock'],['text'=>"✅",'callback_data'=>'lock_sticker']
],
[
  ['text'=>'⚡️ الصور','callback_data'=>'nolock'],['text'=>$_photo,'callback_data'=>'lock_photo']
],
[
  ['text'=>'⚡️ الفيديو','callback_data'=>'nolock'],['text'=>$_video,'callback_data'=>'lock_video']
],
	[
  ['text'=>'⚡️ الصوت','callback_data'=>'nolock'],['text'=>$_voice,'callback_data'=>'lock_voice']
],
	[
  ['text'=>'⚡️ الموسيقى','callback_data'=>'nolock'],['text'=>$_music,'callback_data'=>'lock_music']
],
[
  ['text'=>'⚡️ المتحركه','callback_data'=>'nolock'],['text'=>$_gif,'callback_data'=>'lock_gif']
],
[
  ['text'=>'⚡️ الكلايش ','callback_data'=>'nolock'],['text'=>$_document,'callback_data'=>'lock_document']
],
[
  ['text'=>'⚡️ المواقع ','callback_data'=>'nolock'],['text'=>$_location,'callback_data'=>'lock_location']
],
[
  ['text'=>'⚡️ الجهات ','callback_data'=>'nolock'],['text'=>$_contact,'callback_data'=>'lock_contact']
],
[
  ['text'=>'⚡️ الالعاب ','callback_data'=>'nolock'],['text'=>$_game,'callback_data'=>'lock_game']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_sticker" && $_sticker == "✅"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_media == "❌"){
save("data/$chat_id2/settings/sticker.txt","❌");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'⚡️ الملصقات','callback_data'=>'nolock'],['text'=>"❌",'callback_data'=>'lock_sticker']
],
[
  ['text'=>'⚡️ الصور','callback_data'=>'nolock'],['text'=>$_photo,'callback_data'=>'lock_photo']
],
[
  ['text'=>'⚡️ الفيديو','callback_data'=>'nolock'],['text'=>$_video,'callback_data'=>'lock_video']
],
	[
  ['text'=>'⚡️ الصوت','callback_data'=>'nolock'],['text'=>$_voice,'callback_data'=>'lock_voice']
],
	[
  ['text'=>'⚡️ الموسيقى','callback_data'=>'nolock'],['text'=>$_music,'callback_data'=>'lock_music']
],
[
  ['text'=>'⚡️ المتحركه','callback_data'=>'nolock'],['text'=>$_gif,'callback_data'=>'lock_gif']
],
[
  ['text'=>'⚡️ الكلايش ','callback_data'=>'nolock'],['text'=>$_document,'callback_data'=>'lock_document']
],
[
  ['text'=>'⚡️ المواقع ','callback_data'=>'nolock'],['text'=>$_location,'callback_data'=>'lock_location']
],
[
  ['text'=>'⚡️ الجهات ','callback_data'=>'nolock'],['text'=>$_contact,'callback_data'=>'lock_contact']
],
[
  ['text'=>'⚡️ الالعاب ','callback_data'=>'nolock'],['text'=>$_game,'callback_data'=>'lock_game']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}


   if($data == "lock_photo" && $_photo == "❌"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_media == "❌"){
save("data/$chat_id2/settings/photo.txt","✅");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'⚡️ الملصقات','callback_data'=>'nolock'],['text'=>$_sticker,'callback_data'=>'lock_sticker']
],
[
  ['text'=>'⚡️ الصور','callback_data'=>'nolock'],['text'=>"✅",'callback_data'=>'lock_photo']
],
[
  ['text'=>'⚡️ الفيديو','callback_data'=>'nolock'],['text'=>$_video,'callback_data'=>'lock_video']
],
	[
  ['text'=>'⚡️ الصوت','callback_data'=>'nolock'],['text'=>$_voice,'callback_data'=>'lock_voice']
],
	[
  ['text'=>'⚡️ الموسيقى','callback_data'=>'nolock'],['text'=>$_music,'callback_data'=>'lock_music']
],
[
  ['text'=>'⚡️ المتحركه','callback_data'=>'nolock'],['text'=>$_gif,'callback_data'=>'lock_gif']
],
[
  ['text'=>'⚡️ الكلايش ','callback_data'=>'nolock'],['text'=>$_document,'callback_data'=>'lock_document']
],
[
  ['text'=>'⚡️ المواقع ','callback_data'=>'nolock'],['text'=>$_location,'callback_data'=>'lock_location']
],
[
  ['text'=>'⚡️ الجهات ','callback_data'=>'nolock'],['text'=>$_contact,'callback_data'=>'lock_contact']
],
[
  ['text'=>'⚡️ الالعاب ','callback_data'=>'nolock'],['text'=>$_game,'callback_data'=>'lock_game']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •لقائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_photo" && $_photo == "✅"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_media == "❌"){
save("data/$chat_id2/settings/photo.txt","❌");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'⚡️ الملصقات','callback_data'=>'nolock'],['text'=>$_sticker,'callback_data'=>'lock_sticker']
],
[
  ['text'=>'⚡️ الصور','callback_data'=>'nolock'],['text'=>"❌",'callback_data'=>'lock_photo']
],
[
  ['text'=>'⚡️ الفيديو','callback_data'=>'nolock'],['text'=>$_video,'callback_data'=>'lock_video']
],
	[
  ['text'=>'⚡️ الصوت','callback_data'=>'nolock'],['text'=>$_voice,'callback_data'=>'lock_voice']
],
	[
  ['text'=>'⚡️ الموسيقى','callback_data'=>'nolock'],['text'=>$_music,'callback_data'=>'lock_music']
],
[
  ['text'=>'⚡️ المتحركه','callback_data'=>'nolock'],['text'=>$_gif,'callback_data'=>'lock_gif']
],
[
  ['text'=>'⚡️ الكلايش ','callback_data'=>'nolock'],['text'=>$_document,'callback_data'=>'lock_document']
],
[
  ['text'=>'⚡️ المواقع ','callback_data'=>'nolock'],['text'=>$_location,'callback_data'=>'lock_location']
],
[
  ['text'=>'⚡️ الجهات ','callback_data'=>'nolock'],['text'=>$_contact,'callback_data'=>'lock_contact']
],
[
  ['text'=>'⚡️ الالعاب ','callback_data'=>'nolock'],['text'=>$_game,'callback_data'=>'lock_game']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_video" && $_video == "❌"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_media == "❌"){
save("data/$chat_id2/settings/video.txt","✅");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'⚡️ الملصقات','callback_data'=>'nolock'],['text'=>$_sticker,'callback_data'=>'lock_sticker']
],
[
  ['text'=>'⚡️ الصور','callback_data'=>'nolock'],['text'=>$_photo,'callback_data'=>'lock_photo']
],
[
  ['text'=>'⚡️ الفيديو','callback_data'=>'nolock'],['text'=>"✅",'callback_data'=>'lock_video']
],
	[
  ['text'=>'⚡️ الصوت','callback_data'=>'nolock'],['text'=>$_voice,'callback_data'=>'lock_voice']
],
	[
  ['text'=>'⚡️ الموسيقى','callback_data'=>'nolock'],['text'=>$_music,'callback_data'=>'lock_music']
],
[
  ['text'=>'⚡️ المتحركه','callback_data'=>'nolock'],['text'=>$_gif,'callback_data'=>'lock_gif']
],
[
  ['text'=>'⚡️ الكلايش ','callback_data'=>'nolock'],['text'=>$_document,'callback_data'=>'lock_document']
],
[
  ['text'=>'⚡️ المواقع ','callback_data'=>'nolock'],['text'=>$_location,'callback_data'=>'lock_location']
],
[
  ['text'=>'⚡️ الجهات ','callback_data'=>'nolock'],['text'=>$_contact,'callback_data'=>'lock_contact']
],
[
  ['text'=>'⚡️ الالعاب ','callback_data'=>'nolock'],['text'=>$_game,'callback_data'=>'lock_game']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_video" && $_video == "✅"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_media == "❌"){
save("data/$chat_id2/settings/video.txt","❌");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'⚡️ الملصقات','callback_data'=>'nolock'],['text'=>$_sticker,'callback_data'=>'lock_sticker']
],
[
  ['text'=>'⚡️ الصور','callback_data'=>'nolock'],['text'=>$_photo,'callback_data'=>'lock_photo']
],
[
  ['text'=>'⚡️ الفيديو','callback_data'=>'nolock'],['text'=>"❌",'callback_data'=>'lock_video']
],
	[
  ['text'=>'⚡️ الصوت','callback_data'=>'nolock'],['text'=>$_voice,'callback_data'=>'lock_voice']
],
	[
  ['text'=>'⚡️ الموسيقى','callback_data'=>'nolock'],['text'=>$_music,'callback_data'=>'lock_music']
],
[
  ['text'=>'⚡️ المتحركه','callback_data'=>'nolock'],['text'=>$_gif,'callback_data'=>'lock_gif']
],
[
  ['text'=>'⚡️ الكلايش ','callback_data'=>'nolock'],['text'=>$_document,'callback_data'=>'lock_document']
],
[
  ['text'=>'⚡️ المواقع ','callback_data'=>'nolock'],['text'=>$_location,'callback_data'=>'lock_location']
],
[
  ['text'=>'⚡️ الجهات ','callback_data'=>'nolock'],['text'=>$_contact,'callback_data'=>'lock_contact']
],
[
  ['text'=>'⚡️ الالعاب ','callback_data'=>'nolock'],['text'=>$_game,'callback_data'=>'lock_game']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_voice" && $_voice == "❌"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_media == "❌"){
save("data/$chat_id2/settings/voice.txt","✅");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'⚡️ الملصقات','callback_data'=>'nolock'],['text'=>$_sticker,'callback_data'=>'lock_sticker']
],
[
  ['text'=>'⚡️ الصور','callback_data'=>'nolock'],['text'=>$_photo,'callback_data'=>'lock_photo']
],
[
  ['text'=>'⚡️ الفيديو','callback_data'=>'nolock'],['text'=>$_video,'callback_data'=>'lock_video']
],
	[
  ['text'=>'⚡️ الصوت','callback_data'=>'nolock'],['text'=>"✅",'callback_data'=>'lock_voice']
],
	[
  ['text'=>'⚡️ الموسيقى','callback_data'=>'nolock'],['text'=>$_music,'callback_data'=>'lock_music']
],
[
  ['text'=>'⚡️ المتحركه','callback_data'=>'nolock'],['text'=>$_gif,'callback_data'=>'lock_gif']
],
[
  ['text'=>'⚡️ الكلايش ','callback_data'=>'nolock'],['text'=>$_document,'callback_data'=>'lock_document']
],
[
  ['text'=>'⚡️ المواقع ','callback_data'=>'nolock'],['text'=>$_location,'callback_data'=>'lock_location']
],
[
  ['text'=>'⚡️ الجهات ','callback_data'=>'nolock'],['text'=>$_contact,'callback_data'=>'lock_contact']
],
[
  ['text'=>'⚡️ الالعاب ','callback_data'=>'nolock'],['text'=>$_game,'callback_data'=>'lock_game']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_voice" && $_voice == "✅"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_media == "❌"){
save("data/$chat_id2/settings/voice.txt","❌");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'⚡️ الملصقات','callback_data'=>'nolock'],['text'=>$_sticker,'callback_data'=>'lock_sticker']
],
[
  ['text'=>'⚡️ الصور','callback_data'=>'nolock'],['text'=>$_photo,'callback_data'=>'lock_photo']
],
[
  ['text'=>'⚡️ الفيديو','callback_data'=>'nolock'],['text'=>$_video,'callback_data'=>'lock_video']
],
	[
  ['text'=>'⚡️ الصوت','callback_data'=>'nolock'],['text'=>"❌",'callback_data'=>'lock_voice']
],
	[
  ['text'=>'⚡️ الموسيقى','callback_data'=>'nolock'],['text'=>$_music,'callback_data'=>'lock_music']
],
[
  ['text'=>'⚡️ المتحركه','callback_data'=>'nolock'],['text'=>$_gif,'callback_data'=>'lock_gif']
],
[
  ['text'=>'⚡️ الكلايش ','callback_data'=>'nolock'],['text'=>$_document,'callback_data'=>'lock_document']
],
[
  ['text'=>'⚡️ المواقع ','callback_data'=>'nolock'],['text'=>$_location,'callback_data'=>'lock_location']
],
[
  ['text'=>'⚡️ الجهات ','callback_data'=>'nolock'],['text'=>$_contact,'callback_data'=>'lock_contact']
],
[
  ['text'=>'⚡️ الالعاب ','callback_data'=>'nolock'],['text'=>$_game,'callback_data'=>'lock_game']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_music" && $_music == "❌"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_media == "❌"){
save("data/$chat_id2/settings/music.txt","✅");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'⚡️ الملصقات','callback_data'=>'nolock'],['text'=>$_sticker,'callback_data'=>'lock_sticker']
],
[
  ['text'=>'⚡️ الصور','callback_data'=>'nolock'],['text'=>$_photo,'callback_data'=>'lock_photo']
],
[
  ['text'=>'⚡️ الفيديو','callback_data'=>'nolock'],['text'=>$_video,'callback_data'=>'lock_video']
],
	[
  ['text'=>'⚡️ الصوت','callback_data'=>'nolock'],['text'=>$_voice,'callback_data'=>'lock_voice']
],
	[
  ['text'=>'⚡️ الموسيقى','callback_data'=>'nolock'],['text'=>"✅",'callback_data'=>'lock_music']
],
[
  ['text'=>'⚡️ المتحركه','callback_data'=>'nolock'],['text'=>$_gif,'callback_data'=>'lock_gif']
],
[
  ['text'=>'⚡️ الكلايش ','callback_data'=>'nolock'],['text'=>$_document,'callback_data'=>'lock_document']
],
[
  ['text'=>'⚡️ المواقع ','callback_data'=>'nolock'],['text'=>$_location,'callback_data'=>'lock_location']
],
[
  ['text'=>'⚡️ الجهات ','callback_data'=>'nolock'],['text'=>$_contact,'callback_data'=>'lock_contact']
],
[
  ['text'=>'⚡️ الالعاب ','callback_data'=>'nolock'],['text'=>$_game,'callback_data'=>'lock_game']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_music" && $_music == "✅"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_media == "❌"){
save("data/$chat_id2/settings/music.txt","❌");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'⚡️ الملصقات','callback_data'=>'nolock'],['text'=>$_sticker,'callback_data'=>'lock_sticker']
],
[
  ['text'=>'⚡️ الصور','callback_data'=>'nolock'],['text'=>$_photo,'callback_data'=>'lock_photo']
],
[
  ['text'=>'⚡️ الفيديو','callback_data'=>'nolock'],['text'=>$_video,'callback_data'=>'lock_video']
],
	[
  ['text'=>'⚡️ الصوت','callback_data'=>'nolock'],['text'=>$_voice,'callback_data'=>'lock_voice']
],
	[
  ['text'=>'⚡️ الموسيقى','callback_data'=>'nolock'],['text'=>"❌",'callback_data'=>'lock_music']
],
[
  ['text'=>'⚡️ المتحركه','callback_data'=>'nolock'],['text'=>$_gif,'callback_data'=>'lock_gif']
],
[
  ['text'=>'⚡️ الكلايش ','callback_data'=>'nolock'],['text'=>$_document,'callback_data'=>'lock_document']
],
[
  ['text'=>'⚡️ المواقع ','callback_data'=>'nolock'],['text'=>$_location,'callback_data'=>'lock_location']
],
[
  ['text'=>'⚡️ الجهات ','callback_data'=>'nolock'],['text'=>$_contact,'callback_data'=>'lock_contact']
],
[
  ['text'=>'⚡️ الالعاب ','callback_data'=>'nolock'],['text'=>$_game,'callback_data'=>'lock_game']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}


   if($data == "lock_gif" && $_gif == "❌"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_media == "❌"){
save("data/$chat_id2/settings/gif.txt","✅");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'⚡️ الملصقات','callback_data'=>'nolock'],['text'=>$_sticker,'callback_data'=>'lock_sticker']
],
[
  ['text'=>'⚡️ الصور','callback_data'=>'nolock'],['text'=>$_photo,'callback_data'=>'lock_photo']
],
[
  ['text'=>'⚡️ الفيديو','callback_data'=>'nolock'],['text'=>$_video,'callback_data'=>'lock_video']
],
	[
  ['text'=>'⚡️ الصوت','callback_data'=>'nolock'],['text'=>$_voice,'callback_data'=>'lock_voice']
],
	[
  ['text'=>'⚡️ الموسيقى','callback_data'=>'nolock'],['text'=>$_music,'callback_data'=>'lock_music']
],
[
  ['text'=>'⚡️ المتحركه','callback_data'=>'nolock'],['text'=>"✅",'callback_data'=>'lock_gif']
],
[
  ['text'=>'⚡️ الكلايش ','callback_data'=>'nolock'],['text'=>$_document,'callback_data'=>'lock_document']
],
[
  ['text'=>'⚡️ المواقع ','callback_data'=>'nolock'],['text'=>$_location,'callback_data'=>'lock_location']
],
[
  ['text'=>'⚡️ الجهات ','callback_data'=>'nolock'],['text'=>$_contact,'callback_data'=>'lock_contact']
],
[
  ['text'=>'⚡️ الالعاب ','callback_data'=>'nolock'],['text'=>$_game,'callback_data'=>'lock_game']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_gif" && $_gif == "✅"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_media == "❌"){
save("data/$chat_id2/settings/gif.txt","❌");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'⚡️ الملصقات','callback_data'=>'nolock'],['text'=>$_sticker,'callback_data'=>'lock_sticker']
],
[
  ['text'=>'⚡️ الصور','callback_data'=>'nolock'],['text'=>$_photo,'callback_data'=>'lock_photo']
],
[
  ['text'=>'⚡️ الفيديو','callback_data'=>'nolock'],['text'=>$_video,'callback_data'=>'lock_video']
],
	[
  ['text'=>'⚡️ الصوت','callback_data'=>'nolock'],['text'=>$_voice,'callback_data'=>'lock_voice']
],
	[
  ['text'=>'⚡️ الموسيقى','callback_data'=>'nolock'],['text'=>$_music,'callback_data'=>'lock_music']
],
[
  ['text'=>'⚡️ المتحركه','callback_data'=>'nolock'],['text'=>"❌",'callback_data'=>'lock_gif']
],
[
  ['text'=>'⚡️ الكلايش ','callback_data'=>'nolock'],['text'=>$_document,'callback_data'=>'lock_document']
],
[
  ['text'=>'⚡️ المواقع ','callback_data'=>'nolock'],['text'=>$_location,'callback_data'=>'lock_location']
],
[
  ['text'=>'⚡️ الجهات ','callback_data'=>'nolock'],['text'=>$_contact,'callback_data'=>'lock_contact']
],
[
  ['text'=>'⚡️ الالعاب ','callback_data'=>'nolock'],['text'=>$_game,'callback_data'=>'lock_game']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}


   if($data == "lock_document" && $_document == "❌"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_media == "❌"){
save("data/$chat_id2/settings/document.txt","✅");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'⚡️ الملصقات','callback_data'=>'nolock'],['text'=>$_sticker,'callback_data'=>'lock_sticker']
],
[
  ['text'=>'⚡️ الصور','callback_data'=>'nolock'],['text'=>$_photo,'callback_data'=>'lock_photo']
],
[
  ['text'=>'⚡️ الفيديو','callback_data'=>'nolock'],['text'=>$_video,'callback_data'=>'lock_video']
],
	[
  ['text'=>'⚡️ الصوت','callback_data'=>'nolock'],['text'=>$_voice,'callback_data'=>'lock_voice']
],
	[
  ['text'=>'⚡️ الموسيقى','callback_data'=>'nolock'],['text'=>$_music,'callback_data'=>'lock_music']
],
[
  ['text'=>'⚡️ المتحركه','callback_data'=>'nolock'],['text'=>$_gif,'callback_data'=>'lock_gif']
],
[
  ['text'=>'⚡️ الكلايش ','callback_data'=>'nolock'],['text'=>"✅",'callback_data'=>'lock_document']
],
[
  ['text'=>'⚡️ المواقع ','callback_data'=>'nolock'],['text'=>$_location,'callback_data'=>'lock_location']
],
[
  ['text'=>'⚡️ الجهات ','callback_data'=>'nolock'],['text'=>$_contact,'callback_data'=>'lock_contact']
],
[
  ['text'=>'⚡️ الالعاب ','callback_data'=>'nolock'],['text'=>$_game,'callback_data'=>'lock_game']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_document" && $_document == "✅"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_media == "❌"){
save("data/$chat_id2/settings/document.txt","❌");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'⚡️ الملصقات','callback_data'=>'nolock'],['text'=>$_sticker,'callback_data'=>'lock_sticker']
],
[
  ['text'=>'⚡️ الصور','callback_data'=>'nolock'],['text'=>$_photo,'callback_data'=>'lock_photo']
],
[
  ['text'=>'⚡️ الفيديو','callback_data'=>'nolock'],['text'=>$_video,'callback_data'=>'lock_video']
],
	[
  ['text'=>'⚡️ الصوت','callback_data'=>'nolock'],['text'=>$_voice,'callback_data'=>'lock_voice']
],
	[
  ['text'=>'⚡️ الموسيقى','callback_data'=>'nolock'],['text'=>$_music,'callback_data'=>'lock_music']
],
[
  ['text'=>'⚡️ المتحركه','callback_data'=>'nolock'],['text'=>$_gif,'callback_data'=>'lock_gif']
],
[
  ['text'=>'⚡️ الكلايش ','callback_data'=>'nolock'],['text'=>"❌",'callback_data'=>'lock_document']
],
[
  ['text'=>'⚡️ المواقع ','callback_data'=>'nolock'],['text'=>$_location,'callback_data'=>'lock_location']
],
[
  ['text'=>'⚡️ الجهات ','callback_data'=>'nolock'],['text'=>$_contact,'callback_data'=>'lock_contact']
],
[
  ['text'=>'⚡️ الالعاب ','callback_data'=>'nolock'],['text'=>$_game,'callback_data'=>'lock_game']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}


   if($data == "lock_location" && $_location == "❌"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_media == "❌"){
save("data/$chat_id2/settings/location.txt","✅");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'⚡️ الملصقات','callback_data'=>'nolock'],['text'=>$_sticker,'callback_data'=>'lock_sticker']
],
[
  ['text'=>'⚡️ الصور','callback_data'=>'nolock'],['text'=>$_photo,'callback_data'=>'lock_photo']
],
[
  ['text'=>'⚡️ الفيديو','callback_data'=>'nolock'],['text'=>$_video,'callback_data'=>'lock_video']
],
	[
  ['text'=>'⚡️ الصوت','callback_data'=>'nolock'],['text'=>$_voice,'callback_data'=>'lock_voice']
],
	[
  ['text'=>'⚡️ الموسيقى','callback_data'=>'nolock'],['text'=>$_music,'callback_data'=>'lock_music']
],
[
  ['text'=>'⚡️ المتحركه','callback_data'=>'nolock'],['text'=>$_gif,'callback_data'=>'lock_gif']
],
[
  ['text'=>'⚡️ الكلايش ','callback_data'=>'nolock'],['text'=>$_document,'callback_data'=>'lock_document']
],
[
  ['text'=>'⚡️ المواقع ','callback_data'=>'nolock'],['text'=>"✅",'callback_data'=>'lock_location']
],
[
  ['text'=>'⚡️ الجهات ','callback_data'=>'nolock'],['text'=>$_contact,'callback_data'=>'lock_contact']
],
[
  ['text'=>'⚡️ الالعاب ','callback_data'=>'nolock'],['text'=>$_game,'callback_data'=>'lock_game']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_location" && $_location == "✅"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_media == "❌"){
save("data/$chat_id2/settings/location.txt","❌");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'⚡️ الملصقات','callback_data'=>'nolock'],['text'=>$_sticker,'callback_data'=>'lock_sticker']
],
[
  ['text'=>'⚡️ الصور','callback_data'=>'nolock'],['text'=>$_photo,'callback_data'=>'lock_photo']
],
[
  ['text'=>'⚡️ الفيديو','callback_data'=>'nolock'],['text'=>$_video,'callback_data'=>'lock_video']
],
	[
  ['text'=>'⚡️ الصوت','callback_data'=>'nolock'],['text'=>$_voice,'callback_data'=>'lock_voice']
],
	[
  ['text'=>'⚡️ الموسيقى','callback_data'=>'nolock'],['text'=>$_music,'callback_data'=>'lock_music']
],
[
  ['text'=>'⚡️ المتحركه','callback_data'=>'nolock'],['text'=>$_gif,'callback_data'=>'lock_gif']
],
[
  ['text'=>'⚡️ الكلايش ','callback_data'=>'nolock'],['text'=>$_document,'callback_data'=>'lock_document']
],
[
  ['text'=>'⚡️ المواقع ','callback_data'=>'nolock'],['text'=>"❌",'callback_data'=>'lock_location']
],
[
  ['text'=>'⚡️ الجهات ','callback_data'=>'nolock'],['text'=>$_contact,'callback_data'=>'lock_contact']
],
[
  ['text'=>'⚡️ الالعاب ','callback_data'=>'nolock'],['text'=>$_game,'callback_data'=>'lock_game']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_contact" && $_contact == "❌"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_media == "❌"){
save("data/$chat_id2/settings/contact.txt","✅");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'⚡️ الملصقات','callback_data'=>'nolock'],['text'=>$_sticker,'callback_data'=>'lock_sticker']
],
[
  ['text'=>'⚡️ الصور','callback_data'=>'nolock'],['text'=>$_photo,'callback_data'=>'lock_photo']
],
[
  ['text'=>'⚡️ الفيديو','callback_data'=>'nolock'],['text'=>$_video,'callback_data'=>'lock_video']
],
	[
  ['text'=>'⚡️ الصوت','callback_data'=>'nolock'],['text'=>$_voice,'callback_data'=>'lock_voice']
],
	[
  ['text'=>'⚡️ الموسيقى','callback_data'=>'nolock'],['text'=>$_music,'callback_data'=>'lock_music']
],
[
  ['text'=>'⚡️ المتحركه','callback_data'=>'nolock'],['text'=>$_gif,'callback_data'=>'lock_gif']
],
[
  ['text'=>'⚡️ الكلايش ','callback_data'=>'nolock'],['text'=>$_document,'callback_data'=>'lock_document']
],
[
  ['text'=>'⚡️ المواقع ','callback_data'=>'nolock'],['text'=>$_location,'callback_data'=>'lock_location']
],
[
  ['text'=>'⚡️ الجهات ','callback_data'=>'nolock'],['text'=>"✅",'callback_data'=>'lock_contact']
],
[
  ['text'=>'⚡️ الالعاب ','callback_data'=>'nolock'],['text'=>$_game,'callback_data'=>'lock_game']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_contact" && $_contact == "✅"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_media == "❌"){
save("data/$chat_id2/settings/contact.txt","❌");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'⚡️ الملصقات','callback_data'=>'nolock'],['text'=>$_sticker,'callback_data'=>'lock_sticker']
],
[
  ['text'=>'⚡️ الصور','callback_data'=>'nolock'],['text'=>$_photo,'callback_data'=>'lock_photo']
],
[
  ['text'=>'⚡️ الفيديو','callback_data'=>'nolock'],['text'=>$_video,'callback_data'=>'lock_video']
],
	[
  ['text'=>'⚡️ الصوت','callback_data'=>'nolock'],['text'=>$_voice,'callback_data'=>'lock_voice']
],
	[
  ['text'=>'⚡️ الموسيقى','callback_data'=>'nolock'],['text'=>$_music,'callback_data'=>'lock_music']
],
[
  ['text'=>'⚡️ المتحركه','callback_data'=>'nolock'],['text'=>$_gif,'callback_data'=>'lock_gif']
],
[
  ['text'=>'⚡️ الكلايش ','callback_data'=>'nolock'],['text'=>$_document,'callback_data'=>'lock_document']
],
[
  ['text'=>'⚡️ المواقع ','callback_data'=>'nolock'],['text'=>$_contact,'callback_data'=>'lock_location']
],
[
  ['text'=>'⚡️ الجهات ','callback_data'=>'nolock'],['text'=>"❌",'callback_data'=>'lock_contact']
],
[
  ['text'=>'⚡️ الالعاب ','callback_data'=>'nolock'],['text'=>$_game,'callback_data'=>'lock_game']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_game" && $_game == "❌"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_media == "❌"){
save("data/$chat_id2/settings/game.txt","✅");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'⚡️ الملصقات','callback_data'=>'nolock'],['text'=>$_sticker,'callback_data'=>'lock_sticker']
],
[
  ['text'=>'⚡️ الصور','callback_data'=>'nolock'],['text'=>$_photo,'callback_data'=>'lock_photo']
],
[
  ['text'=>'⚡️ الفيديو','callback_data'=>'nolock'],['text'=>$_video,'callback_data'=>'lock_video']
],
	[
  ['text'=>'⚡️ الصوت','callback_data'=>'nolock'],['text'=>$_voice,'callback_data'=>'lock_voice']
],
	[
  ['text'=>'⚡️ الموسيقى','callback_data'=>'nolock'],['text'=>$_music,'callback_data'=>'lock_music']
],
[
  ['text'=>'⚡️ المتحركه','callback_data'=>'nolock'],['text'=>$_gif,'callback_data'=>'lock_gif']
],
[
  ['text'=>'⚡️ الكلايش ','callback_data'=>'nolock'],['text'=>$_document,'callback_data'=>'lock_document']
],
[
  ['text'=>'⚡️ المواقع ','callback_data'=>'nolock'],['text'=>$_location,'callback_data'=>'lock_location']
],
[
  ['text'=>'⚡️ الجهات ','callback_data'=>'nolock'],['text'=>$_contact,'callback_data'=>'lock_contact']
],
[
  ['text'=>'⚡️ الالعاب ','callback_data'=>'nolock'],['text'=>"✅",'callback_data'=>'lock_game']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}

   if($data == "lock_game" && $_game == "✅"){
				if($admin == $from_id2 || $owner2 == $from_id2 || strpos($modlist2 , "$from_id2") !== false && $_media == "❌"){
save("data/$chat_id2/settings/game.txt","❌");
var_dump(makereq('editMessageText',[
            'chat_id'=>$chat_id2,
            'message_id'=>$message_id2,
  "text" => '- حسنا عزيزي اختر ماتريد قفلةه او فتحه 📬 يمكنك عرض الاوامر الغير شفافة بارسال امر ( الاوامر ) ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'⚡️ الملصقات','callback_data'=>'nolock'],['text'=>$_sticker,'callback_data'=>'lock_sticker']
],
[
  ['text'=>'⚡️ الصور','callback_data'=>'nolock'],['text'=>$_photo,'callback_data'=>'lock_photo']
],
[
  ['text'=>'⚡️ الفيديو','callback_data'=>'nolock'],['text'=>$_video,'callback_data'=>'lock_video']
],
	[
  ['text'=>'⚡️ الصوت','callback_data'=>'nolock'],['text'=>$_voice,'callback_data'=>'lock_voice']
],
	[
  ['text'=>'⚡️ الموسيقى','callback_data'=>'nolock'],['text'=>$_music,'callback_data'=>'lock_music']
],
[
  ['text'=>'⚡️ المتحركه','callback_data'=>'nolock'],['text'=>$_gif,'callback_data'=>'lock_gif']
],
[
  ['text'=>'⚡️ الكلايش ','callback_data'=>'nolock'],['text'=>$_document,'callback_data'=>'lock_document']
],
[
  ['text'=>'⚡️ المواقع ','callback_data'=>'nolock'],['text'=>$_contact,'callback_data'=>'lock_location']
],
[
  ['text'=>'⚡️ الجهات ','callback_data'=>'nolock'],['text'=>$_contact,'callback_data'=>'lock_contact']
],
[
  ['text'=>'⚡️ الالعاب ','callback_data'=>'nolock'],['text'=>"❌",'callback_data'=>'lock_game']
],
[
  ['text'=>'- العودة الى القائمة الرئيسية ☑️ •','callback_data'=>'settings'],
]
]
			])
		]));
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- تم تنفيذ طلبك بنجاح ✅ -",
]);
						}else{
			makereq('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'text'=>"- للادمنيةه او المدراء فقط ⚠️ •",
]);
		}
	}
//-------Start Mute and Unmute by text-------\\
if ($textmessage == 'قفل الجهات' || $textmessage == '/lock contact' || $textmessage == '#mute contact') {
		if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_media2 == "❌"){
		save("data/$chat_id/settings/contact.txt","✅");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم قفل 🏴 الجهات في المجموعةه بنجاح ☑️ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 🔖](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
	'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
}
	if ($textmessage == 'فتح الجهات' || $textmessage == '/unlock contact' || $textmessage == '#unmute contact' ) {
			if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_media2 == "❌"){
		save("data/$chat_id/settings/contact.txt","❌");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم فتح 🏳 الجهات في المجموعةه بنجاح ✅ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 📢](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
	'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
}
if ($textmessage == 'قفل الالعاب' || $textmessage == '/lock game' || $textmessage == '#mute game') {
		if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_media2 == "❌"){
		save("data/$chat_id/settings/game.txt","✅");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم قفل 🏴 الالعاب في المجموعةه بنجاح ☑️ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 🔖](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
	'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
}
	if ($textmessage == 'فتح الالعاب' || $textmessage == '/unlock game' || $textmessage == '#unmute game') {
			if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_media2 == "❌"){
		save("data/$chat_id/settings/game.txt","❌");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم فتح 🏳 الالعاب في المجموعةه بنجاح ✅ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 📢](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
	'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
}

if ($textmessage == 'قفل الملصقات' || $textmessage == '/lock sticker' || $textmessage == '#mute sticker') {
		if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_media2 == "❌"){
		save("data/$chat_id/settings/sticker.txt","✅");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم قفل 🏴 الملصقات في المجموعةه بنجاح ☑️ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 🔖](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
	'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
}

if ($textmessage == 'فتح الملصقات' || $textmessage == '/unlock sticker' || $textmessage == '#unmute sticker') {
	if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_media2 == "❌"){
		save("data/$chat_id/settings/sticker.txt","❌");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم فتح 🏳 الملصقات في المجموعةه بنجاح ✅ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 📢](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
	'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
}
if ($textmessage == 'قفل المواقع' || $textmessage == '/lock location' || $textmessage == '#mute location') {
	if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_media2 == "❌"){
		save("data/$chat_id/settings/location.txt","✅");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم قفل 🏴 المواقع في المجموعةه بنجاح ☑️ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 🔖](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
	'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
}
	if ($textmessage == 'فتح المواقع' || $textmessage == '/unlock location' || $textmessage == '#unmute location' ) {
		if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_media2 == "❌"){
		save("data/$chat_id/settings/location.txt","❌");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم فتح 🏳 الروابط في المجموعةه بنجاح ✅ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 📢](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
	'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
}
if ($textmessage == 'قفل الصور' || $textmessage == '/lock photo' || $textmessage == '#mute photo') {
	if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_media2 == "❌"){
		save("data/$chat_id/settings/photo.txt","✅");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم قفل 🏴 الصور في المجموعةه بنجاح ☑️ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 🔖](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
	'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
}
	if ($textmessage == 'فتح الصور' || $textmessage == '/unlock photo' || $textmessage == '#unmute photo') {
	if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_media2 == "❌"){
		save("data/$chat_id/settings/photo.txt","❌");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم فتح 🏳 الصور في المجموعةه بنجاح ✅ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 📢](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
	'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
}
if ($textmessage == 'قفل الفيديو' || $textmessage == '/lock video' || $textmessage == '#mute video' ) {
	if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_media2 == "❌"){
	save("data/$chat_id/settings/video.txt","✅");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم قفل 🏴 الفيديو في المجموعةه بنجاح ☑️ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 🔖](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
	'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
}
	if ($textmessage == 'فتح الفيديو' || $textmessage == '!unmute video' || $textmessage == '#unmute video') {
		if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_media2 == "❌"){
		save("data/$chat_id/settings/video.txt","❌");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم فتح 🏳 الفيديو في المجموعةه بنجاح ✅ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 📢](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
	'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
}
if ($textmessage == 'قفل الصوت' || $textmessage == '/lock voice' || $textmessage == '#mute voice') {
	if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_media2 == "❌"){
		save("data/$chat_id/settings/voice.txt","✅");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم قفل 🏴 الصوت في المجموعةه بنجاح ☑️ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 🔖](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
	'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
}
	if ($textmessage == 'فتح الصوت' || $textmessage == '/unlock voice' || $textmessage == '#unmute voice') {
		if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_media2 == "❌"){
		save("data/$chat_id/settings/voice.txt","❌");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم فتح 🏳 الصوت في المجموعةه بنجاح ✅ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 📢](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
	'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
}
if ($textmessage == 'قفل البصمه' || $textmessage == '/lock music' || $textmessage == '#mute music') {
		if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_media2 == "❌"){
		save("data/$chat_id/settings/music.txt","✅");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم قفل 🏴 البصمه في المجموعةه بنجاح ☑️ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 🔖](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
	'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
}
	if ($textmessage == 'فتح البصمه' || $textmessage == '/unlock music' || $textmessage == '#unmute music') {
	if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_media2 == "❌"){
		save("data/$chat_id/settings/music.txt","❌");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم فتح 🏳 البصمه في المجموعةه بنجاح ✅ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 📢](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
	'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
}
if ($textmessage == 'قفل المتحركه' || $textmessage == '/lock gif' || $textmessage == '#mute gif') {
		if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_media2 == "❌"){
		save("data/$chat_id/settings/video.txt","✅");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم قفل 🏴 المتحركه في المجموعةه بنجاح ☑️ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 🔖](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
	'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
}
	if ($textmessage == 'فتح المتحركه' || $textmessage == '/unlock gif' || $textmessage == '#unmute gif') {
	if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_media2 == "❌"){
		save("data/$chat_id/settings/gif.txt","❌");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم فتح 🏳 المتحركه في المجموعةه بنجاح ✅ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 📢](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
	'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
}
if ($textmessage == 'قفل الكلايش' || $textmessage == '/lock document' || $textmessage == '#mute document') {
	if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_media2 == "❌"){
	save("data/$chat_id/settings/document.txt","✅");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم قفل 🏴 الكلايش في المجموعةه بنجاح ☑️ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 🔖](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
	'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
}
	if ($textmessage == 'فتح الكلايش' || $textmessage == '/unlock document' || $textmessage == '#unmute document') {
	if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false && $_media2 == "❌"){ 
		save("data/$chat_id/settings/document.txt","❌");
makereq('sendMessage',[
  'chat_id' => $chat_id,
  'text' => '- اهلا عزيزي تم فتح 🏳 الكلايش في المجموعةه بنجاح ✅ -
ֆ • • • • • • • • • • • • • • ֆ
[ • اضغط هنا وتابع جديدنا 📢](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
	'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]
			);
	}
	}
//-------End Mute and UnMute
if ( stripos($username, "Bot" ) !== false || stripos($username, "bot") !== false ) {
		if ($_bot2 == "✅" ) {
			        	makereq('sendMessage',[
            				'chat_id'=>$update->message->chat->id,
            				'text'=>'#ربات_اخراج_شد
										اوردن ربات در گروه ممنوع است. ',
            				'parse_mode'=>'HTML',
            				'reply_to_message_id'=>$update->message->message_id,
            				'disable_web_page_preview'=>true
        				]);
        				makereq('kickChatMember',[
            				'chat_id'=>$update->message->chat->id,
            				'user_id'=>$update->message->from->id
        				]);
			}
		}

	if ($joinmember != null && $wlctext != "" ) {
			        	makereq('sendMessage',[
            				'chat_id'=>$update->message->chat->id,
            				'text'=>"$wlctext",
            				'parse_mode'=>'HTML',
            				'reply_to_message_id'=>$update->message->message_id,
            				'disable_web_page_preview'=>true
        				]);
		}

	if ($leftmember != null && $byetext != "" ) {
			        	makereq('sendMessage',[
            				'chat_id'=>$update->message->chat->id,
            				'text'=>"$byetext",
            				'parse_mode'=>'HTML',
            				'reply_to_message_id'=>$update->message->message_id,
            				'disable_web_page_preview'=>true
        				]);
		}

	$efrom_id = $update->edited_message->from->id;
		$echat_id = $update->edited_message->chat->id;
$eowner = file_get_contents("data/$echat_id/owner.txt");
$emodlist = file_get_contents("data/$echat_id/modlist.txt");
$ewhitelist = file_get_contents("data/$echat_id/whitelist/list.txt");
if($efrom_id !== $admin && $efrom_id != $eowner && $efrom_id != $emodlist && $ewhitelist != $efrom_id){


if ($edit != null) {
		$from_id = $update->edited_message->from->id;
		$chat_id = $update->edited_message->chat->id;
		
	$textmessage = isset($update->edited_message->text)?$update->edited_message->text:'';
	$_link2 = file_get_contents("data/$chat_id/settings/link.txt");
	$_flood2 = file_get_contents("data/$chat_id/settings/flood.txt");
	$_chat2 = file_get_contents("data/$chat_id/settings/chat.txt");
	$_tag2 = file_get_contents("data/$chat_id/settings/tag.txt");
	$_username2 = file_get_contents("data/$chat_id/settings/username.txt");
	$_fwd2 = file_get_contents("data/$chat_id/settings/fwd.txt");
	$_reply2 = file_get_contents("data/$chat_id/settings/reply.txt");
	$_eng2 = file_get_contents("data/$chat_id/settings/eng.txt");
	$_arab2 = file_get_contents("data/$chat_id/settings/arab.txt");
	$_web2 = file_get_contents("data/$chat_id/settings/web.txt");
	$_num2 = file_get_contents("data/$chat_id/settings/num.txt");
		
 if ( stripos($textmessage, "t.me") !== false || stripos($textmessage, "telegram.me") !== false ) {
		if ($_link2 == "✅" ) {
        				makereq('deletemessage',[
                    'chat_id'=>$update->edited_message->chat->id,
            				'message_id'=>$update->edited_message->message_id
        				]);
			}
}

if ( stripos($textmessage, "a" ) !== false || stripos($textmessage, "s") !== false || stripos($textmessage, "d") !== false || stripos($textmessage, "f") !== false || stripos($textmessage, "g") !== false || stripos($textmessage, "h") !== false || stripos($textmessage, "j") !== false || stripos($textmessage, "k") !== false || stripos($textmessage, "l") !== false || stripos($textmessage, "z") !== false || stripos($textmessage, "x") !== false || stripos($textmessage, "c") !== false || stripos($textmessage, "v") !== false || stripos($textmessage, "b") !== false || stripos($textmessage, "n") !== false || stripos($textmessage, "m") !== false || stripos($textmessage, "q") !== false || stripos($textmessage, "w") !== false || stripos($textmessage, "e") !== false || stripos($textmessage, "r") !== false || stripos($textmessage, "t") !== false || stripos($textmessage, "y") !== false || stripos($textmessage, "u") !== false || stripos($textmessage, "i") !== false
|| stripos($textmessage, "o") !== false || stripos($textmessage, "p") !== false) {
		if ($_eng2 == "✅" ) {
        				makereq('deletemessage',[
                    'chat_id'=>$update->edited_message->chat->id,
            				'message_id'=>$update->edited_message->message_id
        				]);
			}
}

if ( stripos($textmessage, "ش" ) !== false || stripos($textmessage, "س") !== false || stripos($textmessage, "ی") !== false || stripos($textmessage, "ب") !== false || stripos($textmessage, "ل") !== false || stripos($textmessage, "ا") !== false || stripos($textmessage, "ت") !== false || stripos($textmessage, "ن") !== false || stripos($textmessage, "م") !== false || stripos($textmessage, "پ") !== false || stripos($textmessage, "ط") !== false || stripos($textmessage, "ظ") !== false || stripos($textmessage, "ز") !== false || stripos($textmessage, "ژ") !== false || stripos($textmessage, "د") !== false || stripos($textmessage, "ر") !== false || stripos($textmessage, "ک") !== false || stripos($textmessage, "و") !== false || stripos($textmessage, "ج") !== false || stripos($textmessage, "گ") !== false || stripos($textmessage, "چ") !== false || stripos($textmessage, "ح") !== false || stripos($textmessage, "ه") !== false || stripos($textmessage, "خ") !== false
|| stripos($textmessage, "ف") !== false || stripos($textmessage, "ع") !== false) {
		if ($_arab2 == "✅" ) {
        				makereq('deletemessage',[
                    'chat_id'=>$update->edited_message->chat->id,
            				'message_id'=>$update->edited_message->message_id
        				]);
			}
}

if (stripos($textmessage, "#") !== false) {
		if ($_tag2 == "✅" ) {
        				makereq('deletemessage',[
                    'chat_id'=>$update->edited_message->chat->id,
            				'message_id'=>$update->edited_message->message_id
        				]);
			}
}

	if (stripos($textmessage, "@") !== false) {
		if ($_username2 == "✅" ) {
        				makereq('deletemessage',[
                    'chat_id'=>$update->edited_message->chat->id,
            				'message_id'=>$update->edited_message->message_id
        				]);
			}
}

if (stripos($textmessage, "1") !== false || stripos($textmessage, "2") !== false || stripos($textmessage, "3") !== false || stripos($textmessage, "4") !== false || stripos($textmessage, "5") !== false || stripos($textmessage, "6") !== false || stripos($textmessage, "7") !== false || stripos($textmessage, "8") !== false || stripos($textmessage, "9") !== false || stripos($textmessage, "0") !== false) {
		if ($_num2 == "✅" ) {
        				makereq('deletemessage',[
                    'chat_id'=>$update->edited_message->chat->id,
            				'message_id'=>$update->edited_message->message_id
        				]);
			}
}

if (stripos($textmessage, "https") !== false || stripos($textmessage, "www") !== false ) {
		if ($_web2 == "✅" ) {
        				makereq('deletemessage',[
                    'chat_id'=>$update->edited_message->chat->id,
            				'message_id'=>$update->edited_message->message_id
        				]);
			}
}
}

if ($edit != null){
				$chat_id = $update->edited_message->chat->id;
			$_edit2 = file_get_contents("data/$chat_id/settings/edit.txt");
	if ($_edit2 == "✅" ) {
        				makereq('deletemessage',[
                    'chat_id'=>$update->edited_message->chat->id,
            				'message_id'=>$update->edited_message->message_id
        				]);
			}
}

}

if($from_id !== $admin && $from_id != $owner && $from_id != $modlist && $whitelist != $from_id){
	
if ( $_flood2 == "✅"){
$timing = date("Y-m-d-h-i-sa");
$timing = str_replace("am","",$timing);

$metti_khan = file_get_contents("flood/$timing-$from_id.txt");
$timing_spam = $metti_khan+1;
file_put_contents("flood/$timing-$from_id.txt","$timing_spam");

$metti_khan2 = file_get_contents("flood/$timing-$from_id.txt");
if($metti_khan2 >= $_floods2  ){
makereq('kickChatMember',[
                    'chat_id'=>$update->message->chat->id,
                    'user_id'=>$update->message->from->id
                ]);
unlink("flood/$timing-$from_id.txt");
return false;
}
}
	
if ( stripos($muteuserlist, "$from_id") !== false ) {
        				makereq('deletemessage',[
            				'chat_id'=>$update->message->chat->id,
            				'message_id'=>$update->message->message_id
        				]);
			}

if ( stripos($textmessage, "t.me") !== false || stripos($textmessage, "telegram.me") !== false ) {
		if ($_link2 == "✅" ) {
        				makereq('deletemessage',[
            				'chat_id'=>$update->message->chat->id,
            				'message_id'=>$update->message->message_id
        				]);
			}
}	

	if ( stripos($textmessage, "a" ) !== false || stripos($textmessage, "s") !== false || stripos($textmessage, "d") !== false || stripos($textmessage, "f") !== false || stripos($textmessage, "g") !== false || stripos($textmessage, "h") !== false || stripos($textmessage, "j") !== false || stripos($textmessage, "k") !== false || stripos($textmessage, "l") !== false || stripos($textmessage, "z") !== false || stripos($textmessage, "x") !== false || stripos($textmessage, "c") !== false || stripos($textmessage, "v") !== false || stripos($textmessage, "b") !== false || stripos($textmessage, "n") !== false || stripos($textmessage, "m") !== false || stripos($textmessage, "q") !== false || stripos($textmessage, "w") !== false || stripos($textmessage, "e") !== false || stripos($textmessage, "r") !== false || stripos($textmessage, "t") !== false || stripos($textmessage, "y") !== false || stripos($textmessage, "u") !== false || stripos($textmessage, "i") !== false
|| stripos($textmessage, "o") !== false || stripos($textmessage, "p") !== false) {
		if ($_eng2 == "✅" ) {
        				makereq('deletemessage',[
            				'chat_id'=>$update->message->chat->id,
            				'message_id'=>$update->message->message_id
        				]);
			}
}

if ( stripos($textmessage, "ش" ) !== false || stripos($textmessage, "س") !== false || stripos($textmessage, "ی") !== false || stripos($textmessage, "ب") !== false || stripos($textmessage, "ل") !== false || stripos($textmessage, "ا") !== false || stripos($textmessage, "ت") !== false || stripos($textmessage, "ن") !== false || stripos($textmessage, "م") !== false || stripos($textmessage, "پ") !== false || stripos($textmessage, "ط") !== false || stripos($textmessage, "ظ") !== false || stripos($textmessage, "ز") !== false || stripos($textmessage, "ژ") !== false || stripos($textmessage, "د") !== false || stripos($textmessage, "ر") !== false || stripos($textmessage, "ک") !== false || stripos($textmessage, "و") !== false || stripos($textmessage, "ج") !== false || stripos($textmessage, "گ") !== false || stripos($textmessage, "چ") !== false || stripos($textmessage, "ح") !== false || stripos($textmessage, "ه") !== false || stripos($textmessage, "خ") !== false
|| stripos($textmessage, "ف") !== false || stripos($textmessage, "ع") !== false) {
		if ($_arab2 == "✅" ) {
        				makereq('deletemessage',[
                    'chat_id'=>$update->message->chat->id,
            				'message_id'=>$update->message->message_id
        				]);
			}
}

if (stripos($textmessage, "#") !== false) {
		if ($_tag2 == "✅" ) {
        				makereq('deletemessage',[
                    'chat_id'=>$update->message->chat->id,
            				'message_id'=>$update->message->message_id
        				]);
			}
}

	if (stripos($textmessage, "@") !== false) {
		if ($_username2 == "✅" ) {
        				makereq('deletemessage',[
                    'chat_id'=>$update->message->chat->id,
            				'message_id'=>$update->message->message_id
        				]);
			}
}

if ($textmessage != null) {
		if ($_chat2 == "✅" ) {
        				makereq('deletemessage',[
                    'chat_id'=>$update->message->chat->id,
            				'message_id'=>$update->message->message_id
        				]);
			}
}

if (stripos($textmessage, "1") !== false || stripos($textmessage, "2") !== false || stripos($textmessage, "3") !== false || stripos($textmessage, "4") !== false || stripos($textmessage, "5") !== false || stripos($textmessage, "6") !== false || stripos($textmessage, "7") !== false || stripos($textmessage, "8") !== false || stripos($textmessage, "9") !== false || stripos($textmessage, "0") !== false) {
		if ($_num2 == "✅" ) {
        				makereq('deletemessage',[
                    'chat_id'=>$update->message->chat->id,
            				'message_id'=>$update->message->message_id
        				]);
			}
}

if (stripos($textmessage, "https") !== false || stripos($textmessage, "www") !== false ) {
		if ($_web2 == "✅" ) {
        				makereq('deletemessage',[
                    'chat_id'=>$update->message->chat->id,
            				'message_id'=>$update->message->message_id
        				]);
			}
}

		if (strpos($filterlist , $textmessage) !== false) {
		if ($from_id !== $admin && $from_id !== $owner && $from_id != $modlist && $whitelist != $from_id) {
        				makereq('deletemessage',[
                    'chat_id'=>$update->message->chat->id,
            				'message_id'=>$update->message->message_id
        				]);
			}
}
	

	if ($forward != null) {
		if ($_fwd2 == "✅" ) {
        				makereq('deletemessage',[
                    'chat_id'=>$update->message->chat->id,
            				'message_id'=>$update->message->message_id
        				]);
			}
}

	if ($game != null) {
		if ($_game2 == "✅" ) {
        				makereq('deletemessage',[
                    'chat_id'=>$update->message->chat->id,
            				'message_id'=>$update->message->message_id
        				]);
			}
}

	if ($contact != null) {
		if ($_contact2 == "✅" ) {
        				makereq('deletemessage',[
                    'chat_id'=>$update->message->chat->id,
            				'message_id'=>$update->message->message_id
        				]);
			}
}

	if ($photo != null) {
		if ($_photo2 == "✅" ) {
        				makereq('deletemessage',[
                    'chat_id'=>$update->message->chat->id,
            				'message_id'=>$update->message->message_id
        				]);
			}
}

if ($location != null) {
		if ($_location2 == "✅" ) {
        				makereq('deletemessage',[
                    'chat_id'=>$update->message->chat->id,
            				'message_id'=>$update->message->message_id
        				]);
			}
}

	if ($sticker != null) {
		if ($_sticker2 == "✅" ) {
        				makereq('deletemessage',[
                    'chat_id'=>$update->message->chat->id,
            				'message_id'=>$update->message->message_id
        				]);
			}
}

	if ($video != null) {
		if ($_video2 == "✅" ) {
        				makereq('deletemessage',[
                    'chat_id'=>$update->message->chat->id,
            				'message_id'=>$update->message->message_id
        				]);
			}
}

	if ($voice != null) {
		if ($_voice2 == "✅" ) {
        				makereq('deletemessage',[
                    'chat_id'=>$update->message->chat->id,
            				'message_id'=>$update->message->message_id
        				]);
			}
}

if ($music != null) {
		if ($_music2 == "✅" ) {
        				makereq('deletemessage',[
                    'chat_id'=>$update->message->chat->id,
            				'message_id'=>$update->message->message_id
        				]);
			}
}

	if ($gif != null) {
		if ($_gif2 == "✅" ) {
        				makereq('deletemessage',[
                    'chat_id'=>$update->message->chat->id,
            				'message_id'=>$update->message->message_id
        				]);
			}
}

	if ($document != null) {
		if ($_document2 == "✅" ) {
        				makereq('deletemessage',[
                    'chat_id'=>$update->message->chat->id,
            				'message_id'=>$update->message->message_id
        				]);
			}
}

	if ($reply != null) {
		if ($_reply2 == "✅" ) {
        				makereq('deletemessage',[
                    'chat_id'=>$update->message->chat->id,
            				'message_id'=>$update->message->message_id
        				]);
			}
}
	
}

if ($textmessage == "/kickme" || $textmessage == "!kickme" || $textmessage == "#kickme") {
makereq('kickChatMember',[
            				'chat_id'=>$update->message->chat->id,
            				'user_id'=>$update->message->from->id
        				]);
}

if ($textmessage == "/leave" && $from_id == $admin ) {
makereq('leaveChat',[
	'chat_id'=>$chat_id
	]);
	}

if ( $_lockcmd2 == "❌" || $admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false || $type2 == "private") {

if ($textmessage == "/id" || $textmessage == "!id" || $textmessage == "#id") {
			if (!file_exists("data/$chat_id/member/".$from_id."3.txt")) {
			save("data/$chat_id/member/".$from_id."3.txt","0");
}
			$ekhtart3 = -1;
				$fp = fopen( "data/$chat_id/member/".$from_id."3.txt", 'r');
	while( !feof( $fp)) {
    		fgets( $fp);
    		$ekhtart3 ++;
	}
makereq('sendMessage',[
  'chat_id' => $update->message->chat->id,
  "text" => '<b>-----Your Info-----</b>

👤<b>Name</b> : '.$name.'

🆔<b>UserName</b> : <a href="t.me/'.$username.'">@'.$username.'</a>

🆔<b>ID</b> : '.$from_id.'

<b>-----Group Info-----</b>

👥<b>Group Name</b> : '.$gpname.'

🆔<b>Group ID</b> : '.$chat_id.'

👥<b>Group Type</b> : '.$type2.' 

<b>-----Warn Info-----</b>

👮Warn From Admin 
'.$ekhtart3.'|'.$warnlists.' ',
            	'parse_mode'=>'HTML',
              'reply_to_message_id'=>$update->message->message_id,
            	'disable_web_page_preview'=>true
            	]);
}

if ($textmessage == 'الاعدادات' || $textmessage == 'اعدادات'.$botusername.'') {
if($type2 == "supergroup" || $type2 == "group" ){
 makereq('sendMessage',[
        	'chat_id'=>$chat_id,
        	'text'=>"- تم ارسال قائمةه الاعدادات 📬 اليك عبر رسالة في الخاص اذا لم تاتيك ⚡️ رسالة ارسل للبوت ستارت ⚠️ -",
            	'parse_mode'=>'HTML',
              'reply_to_message_id'=>$update->message->message_id,
            	'disable_web_page_preview'=>true
                
            	]);
			if (!file_exists("data/$chat_id/member/".$from_id."3.txt")) {
			save("data/$chat_id/member/".$from_id."3.txt","0");
}
			$ekhtart3 =-1;
				$fp = fopen( "data/$chat_id/member/".$from_id."3.txt", 'r');
	while( !feof( $fp)) {
    		fgets( $fp);
    		$ekhtart3 ++;
	}
var_dump(makereq('sendMessage',[
  'chat_id' => $update->message->from->id,
  "text" => '- حسنا عزيزي هذه قائمة الاعدادات 📬 الخاصةه بمجموعتك ⚠️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
- ❌ = مفتوح •
- ✅ = مقفول •',
  'parse_mode'=>"Markdown",
'reply_markup' =>json_encode([
'inline_keyboard'=>[
[
  ['text'=>'- الاعدادات العامةه ⚠️ -','callback_data'=>'nolock'],
],
[
  ['text'=>'🏷 التكرار','callback_data'=>'nolock'],['text'=>$_flood2,'callback_data'=>'lock']
],
		[
  ['text'=>'🏷 التكرار','callback_data'=>'nolock'],['text'=>$_floods2,'callback_data'=>'lock_floods']
],
[
  ['text'=>'🏷 الروابط','callback_data'=>'nolock'],['text'=>$_link2,'callback_data'=>'lock']
],
[
  ['text'=>'🏷 التاك','callback_data'=>'nolock'],['text'=>$_tag2,'callback_data'=>'lock']
],
[
  ['text'=>'🏷 المعرف','callback_data'=>'nolock'],['text'=>$_username2,'callback_data'=>'lock']
],
[
  ['text'=>'🏷 الارقام','callback_data'=>'nolock'],['text'=>$_num2,'callback_data'=>'lock']
],
[
  ['text'=>'🏷 الويب','callback_data'=>'nolock'],['text'=>$_web2,'callback_data'=>'lock']
],
[
  ['text'=>'🏷 الدردشة','callback_data'=>'nolock'],['text'=>$_chat2,'callback_data'=>'lock']
],
[
  ['text'=>'🏷 التوجيه','callback_data'=>'nolock'],['text'=>$_fwd2,'callback_data'=>'lock']
],
	[
  ['text'=>'🏷 الرد','callback_data'=>'nolock'],['text'=>$_reply2,'callback_data'=>'lock']
],
	[
  ['text'=>'🏷 التعديل','callback_data'=>'nolock'],['text'=>$_edit2,'callback_data'=>'lock']
],
[
  ['text'=>'🏷 الانجليزية','callback_data'=>'nolock'],['text'=>$_eng2,'callback_data'=>'lock']
],
[
  ['text'=>'🏷 العربية','callback_data'=>'nolock'],['text'=>$_arab2,'callback_data'=>'lock']
],
[
  ['text'=>'🏷 الانضمام','callback_data'=>'nolock'],['text'=>$_join2,'callback_data'=>'lock']
],
[
  ['text'=>'🏷 البوتات','callback_data'=>'nolock'],['text'=>$_bot2,'callback_data'=>'lock']
],
		[
  ['text'=>'🏷 المغادرة','callback_data'=>'nolock'],['text'=>$_kickme2,'callback_data'=>'lock']
],
[
  ['text'=>'- اعدادات الميديا 🔖 -','callback_data'=>'nolock'],
],
[
  ['text'=>'⚡️ الملصقات','callback_data'=>'nolock'],['text'=>$_sticker2,'callback_data'=>'lock']
],
[
  ['text'=>'⚡️ الصور','callback_data'=>'nolock'],['text'=>$_photo2,'callback_data'=>'lock']
],
[
  ['text'=>'⚡️ الفيديو','callback_data'=>'nolock'],['text'=>$_video2,'callback_data'=>'lock']
],
	[
  ['text'=>'⚡️ الصوت','callback_data'=>'nolock'],['text'=>$_voice2,'callback_data'=>'lock']
],
	[
  ['text'=>'⚡️ البصمه','callback_data'=>'nolock'],['text'=>$_music2,'callback_data'=>'lock']
],
[
  ['text'=>'⚡️ المتحركه','callback_data'=>'nolock'],['text'=>$_gif2,'callback_data'=>'lock']
],
[
  ['text'=>'⚡️ الكلايش ','callback_data'=>'nolock'],['text'=>$_document2,'callback_data'=>'lock']
],
[
  ['text'=>'⚡️ المواقع ','callback_data'=>'nolock'],['text'=>$_location2,'callback_data'=>'lock']
],
[
  ['text'=>'⚡️ الجهات ','callback_data'=>'nolock'],['text'=>$_contact2,'callback_data'=>'lock']
],
[
  ['text'=>'⚡️ الالعاب ','callback_data'=>'nolock'],['text'=>$_game2,'callback_data'=>'lock']
],
		[
  ['text'=>'- اضغط هنا وتابع جديدنا ✅ -','url'=>'https://telegram.me/'.$channel.''],
]
]
			])
		]));
	
	}
}
	

$rnd = rand(1,999999999999999999);
if($text=="معلوماتي" or $text == "ايدي" and in_array($chat_id, $gpuse) and $type == "supergroup"){
$re = makereq("getUserProfilePhotos",["user_id"=>$id,"limit"=>1,"offset"=>0]);
$res = $re->result->photos[0][2]->file_id;
$pa = makereq("getFile",["file_id"=>$res]);
$path = $pa->result->file_path;
file_put_contents("$rnd.jpg",file_get_contents("https://api.telegram.org/file/bot".$API_KEY."/".$path));
$uphoto = "https://dane-maxbot.000webhostapp.com//$rnd.jpg"; // رابط استضافتك
makereq("sendPhoto",[
'chat_id'=>$chat_id,
"photo"=>$uphoto,
'caption'=>"• ايدي المجموعةه 📡 : $gpid
• ايديك 🖱 : $id
• معرفك 🕸 : @$username
• اسمك 💧: $name
• رسائل المجموعةه 🍥 : $message->message_id",
'reply_to_message_id'=>$messid,
'reply_markup'=>json_encode([
            'inline_keyboard'=>[
               [
              ["text"=>"• قناة البوت 📡 •",'url'=>"https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA"], 
              ]
              ]
        ])
]);
unlink("$rnd.jpg");
}


if ($textmessage == "ايدي" || $textmessage == "/me" || $textmessage == "موقعي") {
makereq('sendPhoto',[
 'chat_id' => $update->message->chat->id,
 'photo' => $getuserphoto,
 'caption' => '
👤اسمك : '.$name.'

🆔معرفك : @'.$username.'

🆔ايديك : '.$from_id.'

🆔عدد صورك الشخصيةه : '.$cuphoto.' ',
              'reply_to_message_id'=>$update->message->message_id,
            	]);
}	
	

if ($textmessage == "تحذيراتي" || $textmessage == "/mywarn" || $textmessage == "#mywarn") {
			if (!file_exists("data/$chat_id/member/".$from_id."3.txt")) {
			save("data/$chat_id/member/".$from_id."3.txt","0");
}
			$ekhtart3 = -1;
				$fp = fopen( "data/$chat_id/member/".$from_id."3.txt", 'r');
	while( !feof( $fp)) {
    		fgets( $fp);
    		$ekhtart3 ++;
	}
makereq('sendMessage',[
  'chat_id' => $update->message->chat->id,
  "text" => '<b>-----عدد تحذيراتك-----</b>
'.$ekhtart3.'|'.$warnlists.' ',
            	'parse_mode'=>'HTML',
              'reply_to_message_id'=>$update->message->message_id,
            	'disable_web_page_preview'=>true
            	]);
}
	
	if(preg_match('موقع (.*)',$textmessage)){
	preg_match('موقع (.*)',$textmessage,$match);
	$location = json_decode(file_get_contents("http://maps.googleapis.com/maps/api/geocode/json?address=".$match[2]));
	makereq('sendLocation',[
    'chat_id'=>$chat_id,
    'latitude'=>$location->results[0]->geometry->location->lat,
	'longitude'=>$location->results[0]->geometry->location->lng
  ]);
  }
  
	if ( strpos($textmessage , 'جلب صوره ') !== false  ) {
$text = str_replace("جلب صوره ","",$textmessage);
makereq('sendPhoto',[
 'chat_id' => $update->message->chat->id,
 'photo' =>$getuserprofile->photos[$text-1][0]->file_id,
 'caption' => '
👤 صوره رقم : '.$text.'

🆔 عدد صورك الشخصيةه : '.$cuphoto.' ',
              'reply_to_message_id'=>$update->message->message_id,
            	]);
}	
	
}

if ($textmessage == '/start' && $type2 == "private" ) {
		$userlist = file_get_contents("users.txt");
	 if (strpos($userlist , "$from_id") == false){
 $txxt = file_get_contents('users.txt');
    $pmembersid= explode("\n",$txxt);
    if (!in_array($from_id,$pmembersid)){
      $aaddd = file_get_contents('users.txt');
      $aaddd .= $from_id."\n";
  file_put_contents('users.txt',$aaddd);
    }
	}
var_dump(makereq('sendMessage',[
        	'chat_id'=>$chat_id,
        	'text'=>"• اهلا بك عزيزي [$name](https://t.me/joinchat/AAAAAEDJCeBNNDdScN-_sg) ⚡️ •

         ֆ • • • • • • • • • • • • • • • • ֆ

- في بوت حمايةه المجموعات 📬 -

- يمكنك من خلال هذا البوت ان تحمي مجموعتك الخاصةه من ( الروابط , التوجيه , الملصقات , الخ . . . ) ☑️

• اضف البوت لمجموعتك ارفع البوت ادمن في المجموعةه 🏴 !! -

• ارسل كلمة ( تفعيل ) في المجموعةه اكتب الاوامر في المجموعةه لاضهار الاوامر ✅ -

• بعد قفل الميديا اكتب ( الاعدادات ) لمعرفة الاوامر المقفولة والمفتوحه ⚠️ -

         ֆ • • • • • • • • • • • • • • • • ֆ

[- اضغط هنا وتابع قناة البوت 🔖](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)",
              'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id,
              'reply_markup' =>json_encode([
              'inline_keyboard'=>[
[
  ['text'=>'- تابع قناة البوت 📡 -','url'=>'https://telegram.me/'.$channel.''],
],
[
  ['text'=>'- اضغط هنا لمراسلة المطور 📬 •','url'=>'t.me/pro_co'],
],
[
  ['text'=>'• اضغط هنا 🏴 •','url'=>'https://t.me/joinchat/AAAAAEDJCeBNNDdScN-_sg'],
]
	]
	])
    		]));
}


if ($textmessage == 'ping' || $textmessage == 'تيست' || $textmessage == 'تجربه' || $textmessage == 'شغال') {
		if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false){
makereq('sendMessage',[
        	'chat_id'=>$chat_id,
        	'text'=>"-` البوت شغال ياعزيزي ✅` -",
            	'parse_mode'=>'MarkDown',
              'reply_to_message_id'=>$update->message->message_id,
              'reply_markup' =>json_encode([
              'inline_keyboard'=>[
[
  ['text'=>'- اضغط هنا وتابع جديدنا 📬 -','url'=>'https://telegram.me/'.$channel.''],
]
	]
	])
	]);
}
}

$memb = $message->new_chat_member; 
if($memb) {
makereq('sendMessage',[
'chat_id'=>$chat_id,
'text'=>"
اهلا بك عزيزي
[- اضغط هنا وتابع جديدنا 💛](https://t.me/joinchat/AAAAAEDJCeBNNDdScN-_sg)",
'reply_to_message_id'=>$message->message_id,
'disable_web_page_preview'=>true,
'parse_mode'=>"MarkDown",
  'reply_markup'=>json_encode([
            'inline_keyboard'=>[
              [
        ['text'=>"- تابع قناة البوت ☑ -",'url'=>"https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA"],
              ]
              ]
        ])
]);
}

if ($textmessage == 'add' || $textmessage == 'فعل' || $textmessage == 'تفعيل' || $textmessage == '/add') {
		if ($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false){
makereq('sendMessage',[
        	'chat_id'=>$chat_id,
        	'text'=>"- تم تفعيل البوت 🏴 في المجموعةه •
- لرؤية الاوامر ارسل الاوامر ☑️ •
- لرؤية الاعدادات ارسل الاعدادات 📂 •
ֆ • • • • • • • • • • • • • • ֆ
[- اضغط هنا وتابع قناة البوت ⚠️](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)",
            	'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
              'reply_to_message_id'=>$update->message->message_id,
              'reply_markup' =>json_encode([
              'inline_keyboard'=>[
[
  ['text'=>'- اضغط هنا وتابع جديدنا 📬 -','url'=>'https://telegram.me/'.$channel.''],
]
	]
	])
	]);
}
}

if ($textmessage == 'الاوامر' || $textmessage == '/help' || $textmessage == '/الاوامر' || $textmessage == 'مساعدة'.$botusername.'') {
if($type2 == "supergroup" || $type2 == "group"){
if($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false){
makereq('sendMessage',[
        	'chat_id'=>$chat_id,
        	'text'=>'	• اهلا بك عزيزي في قائمة الاوامر ⚠️ •

        ֆ • • • • • • • • • • • • • • • • ֆ

- م1 || h1 : لرؤيةه اوامر الادارة 📝 •
- م2 || h2 : لرؤية اوامر اعدادات المجموعة ⚙️ •

- م3 || h3 : لرؤية اوامر الخاصة بالقفل 🔱 •
- م4 || h4 : لرؤية الاوامر الخاصة بالفتح 🏴 •

- م5 || h5 : لرؤية الاوامر العامةه للمجموعةه 📌 •
- م6 || h6 : لرؤية الاوامر بالازرار الشفافةه الميديا وغيرها 📂 •

        ֆ • • • • • • • • • • • • • • • • ֆ
#تستطيع استخدام او روئية الاوامر بالاعدادات الاختيارية ↘️ֆ -
        اي بالـ *Ar* & *En* ☑️ •
        ֆ • • • • • • • • • • • • • • • • ֆ
[- اضغط هنا وتابع قناة البوت 📬](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
		'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id,
    		]);
}
}
}

if ($textmessage == '/h1' || $textmessage == 'h1' || $textmessage == 'م1' || $textmessage == '/م1'.$botusername.'') {
if($type2 == "supergroup" || $type2 == "group"){
if($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false){
makereq('sendMessage',[
        	'chat_id'=>$chat_id,
        	'text'=>'	• اهلا بك عزيزي في قائمه اوامر الادارة 📝 •
    
        ֆ • • • • • • • • • • • • • • • • ֆ
- منع + لكلمه  : لمنع لكلمه في للمجموعة الخاصة بك 🔁 •

- القوانين | /rules : لاضهار قوانين مجموعتك الخاصةه 📌 •

- ضع قوانين || /setrules + القوانين : لوضع قوانين لل مجموعةه 🔗 •

- مسح القوانين || /delrules : لمسح القوانين الخاصة بالمجموعة ☑️ •

- الرابط | /link : لاضهار رابط المجموعة الخاصة بك 📖 •

- ضع رابط | /setlink + الرابط : لوضع رابط للمجموعة 💬  •

- ايدي || /id : لاضهار ايديك ومعلومات حسابك 📬 -

- موقع + المنطقة : لاضهار المنطقة على الخريطه من خلال البوت ⚡️ -
- ضع ترحيب || /setwlc + الترحيب : لوضع ترحيب في المجموعة ⚡️ •

- مسح الترحيب || /delwlc : لمسح الترحيب الخاص بمجموعتك 🚸 •

- ضع توديع || /setbye + التوديع : لوضع توديع في المجموعة ⚠️ •

- مسح التوديع || /delbye : لمسح التوديع الخاص بالمجموعةه ✅ •

- ضع تكرار || /setflood + العدد : لوضع عدد تكرار رسائل في المجموعةه 🌪 •
         ֆ • • • • • • • • • • • • • • • • ֆ
#تستطيع استخدام او روئية الاوامر بالاعدادات الاختيارية ↘️ֆ -
        اي بالـ *Ar* & *En* ☑️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
[- اضغط هنا وتابع قناة البوت 📬](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
		'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id,
    		]);
}
}
}

if ($textmessage == '/h3' || $textmessage == 'h3' || $textmessage == 'م3' || $textmessage == '/م3'.$botusername.'') {
if($type2 == "supergroup" || $type2 == "group"){
if($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false){
makereq('sendMessage',[
        	'chat_id'=>$chat_id,
        	'text'=>'• اهلا بك عزيزي ⚡️ في قائمه اوامر القفل ⚠️ •
- قفل // lock 💬 •

         ֆ • • • • • • • • • • • • • • • • ֆ

- التعديل // edit ⚡️ •
- البوتات // bots 🔖 •
- التكرار // flood 💧 •

- البصمه // music 🔥 •
- الدردشه // chat ☄ •
- المواقع // web 🌪 •

- الفيديو // video 📊 •
- الصور // photo 🖱 •
- المتحركه // gif 🍥 •

- الرد // replay 🌾 •
- الصوت // voice 🕸 •
- الروابط // links 🌙 •

- الويب // web ⚠️ •
- المعرف // username❕•
- الجهات //contact ✅ •

- التاك // tag ♦️ •
- العربيه // arabic 🚸 •
- الانجليزيه // english 💭 •

- الملصقات // stickers 📬 •
- التوجيه // forward 📡 •
- الاشعارات // join ⚡️ •

- الالعاب // game 📈 •
- الكلايش // document 🔬 •
- المغادرة // kickme ✨ •

          ֆ • • • • • • • • • • • • • • • • ֆ
#تستطيع استخدام او روئية الاوامر بالاعدادات الاختيارية ↘️ֆ -
        اي بالـ *Ar* & *En* ☑️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
[- اضغط هنا وتابع قناة البوت 📬](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
		'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id,
    		]);
}
}
}

if ($textmessage == '/h4' || $textmessage == 'h4' || $textmessage == 'م4' || $textmessage == '/م4'.$botusername.'') {
if($type2 == "supergroup" || $type2 == "group"){
if($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false){
makereq('sendMessage',[
        	'chat_id'=>$chat_id,
        	'text'=>'• اهلا بك عزيزي ☑️ في قائمه اوامر الفتح 📬 •
- فتح // unlock 💬 •

         ֆ • • • • • • • • • • • • • • • • ֆ

- التعديل // edit ⚡️ •
- البوتات // bots 🔖 •
- التكرار // flood 💧 •

- البصمه // music 🔥 •
- الدردشه // chat ☄ •
- المواقع // web 🌪 •

- الفيديو // video 📊 •
- الصور // photo 🖱 •
- المتحركه // gif 🍥 •

- الرد // replay 🌾 •
- الصوت // voice 🕸 •
- الروابط // links 🌙 •

- الويب // web ⚠️ •
- المعرف // username❕•
- الجهات //contact ✅ •

- التاك // tag ♦️ •
- العربيه // arabic 🚸 •
- الانجليزيه // english 💭 •

- الملصقات // stickers 📬 •
- التوجيه // forward 📡 •
- الاشعارات // join ⚡️ •

- الالعاب // game 📈 •
- الكلايش // document 🔬 •
- المغادرة // kickme ✨ •

          ֆ • • • • • • • • • • • • • • • • ֆ
#تستطيع استخدام او روئية الاوامر بالاعدادات الاختيارية ↘️ֆ -
        اي بالـ *Ar* & *En* ☑️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
[- اضغط هنا وتابع قناة البوت 📬](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
		'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id,
    		]);
}
}
}

if ($textmessage == '/h5' || $textmessage == 'h5' || $textmessage == 'م5' || $textmessage == '/م5'.$botusername.'') {
if($type2 == "supergroup" || $type2 == "group"){
if($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false){
makereq('sendMessage',[
        	'chat_id'=>$chat_id,
        	'text'=>'	• اهلا بك عزيزي في الاوامر العامةه 🏴 •

         ֆ • • • • • • • • • • • • • • • • ֆ
- كتم || /muteuaer : بالرد او المعرف لكتم العضو 🏳 •

- الغاء كتم || /unmuteuser : بالرد او المعرف لالغاء كتم العضو 📄 •

- حظر || /ban : بالرد او المعرف لحظر العضو من المجموعه 📋 •

- الغاء حظر || /unban : بالرد او المعرف لالغاء حظره من المجموعه 🎵 •

- مسح || /del : بالرد على الرسالةه لمسحها من المجموعةه 🎧 •

- معلومات || /info : بالرد لاضهار معلومات العضو في المجموعةه 📂 •

- مغادرة || /kickme : اذا اردت لمغادرة سوف يقوم البوت بطردك 🔄 •

- منع + الكلمه : لمنعها ✨ •
- الغاء منع + الكلمه : لالغاء منعها 💥 •
- قائمه المنع : لرؤية الكلمات الممنوعه ⚡️ •

- طرد || /kick : بالرد لطرد العضو من المجموعةه الخاصةه بك 🌪 •
         ֆ • • • • • • • • • • • • • • • • ֆ
#تستطيع استخدام او روئية الاوامر بالاعدادات الاختيارية ↘️ֆ -
        اي بالـ *Ar* & *En* ☑️ •
         ֆ • • • • • • • • • • • • • • • • ֆ
[- اضغط هنا وتابع قناة البوت 📬](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
		'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id,
    		]);
}
}
}

if ($textmessage == '/h2' || $textmessage == 'h2' || $textmessage == 'م2' || $textmessage == '/م2'.$botusername.'') {
if($type2 == "supergroup" || $type2 == "group"){
if($admin == $from_id || $owner == $from_id || strpos($modlist , "$from_id") !== false){
makereq('sendMessage',[
        	'chat_id'=>$chat_id,
        	'text'=>'	• اهلا بك عزيزي في قائمة اوامر الرفع 🏳 •
- ملاحظه : منشى المجموعةه والمطور فقط يمكنه رفع الاعضاء ↘️ •

        ֆ • • • • • • • • • • • • • • • • ֆ
- رفع مدير || /setowner : بالرد او المعرف لرفع مدير في البوت 🏴 •

- تنزيل مدير || /delowner : بالرد او المعرف لتنزيلة من المدراء 🕷 •

- رفع ادمن || /setmote : بالرد او المعرف لرفع ادمن في البوت 🐾 •

- تنزيل ادمن || /delmote : بالرد او المعرف لتنزيله من الادمنيةه 📌 •

- المدراء : لاضهار قائمه المدراء 📂 •
- الادمنيه : لاضهار قائمه الادمنيه 🌪 •

        ֆ • • • • • • • • • • • • • • • • ֆ
#تستطيع استخدام او روئية الاوامر بالاعدادات الاختيارية ↘️ֆ -
        اي بالـ Ar & En ☑️ •
        ֆ • • • • • • • • • • • • • • • • ֆ
[- اضغط هنا وتابع قناة البوت 📬](https://t.me/joinchat/AAAAAEOUTmy2w5Mf0KNEKA)',
		'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id,
    		]);
}
}
}

if ($textmessage == 'معلومات البوت' || $textmessage == '!معلومات البوت' || $textmessage == '#معلومات البوت') {
if($type2 == "supergroup" || $type2 == "group"){
makereq('sendMessage',[
        	'chat_id'=>$chat_id,
        	'text'=>'• معلومات البوت هي ⚡️ :-: 
- الاسم 📬 : '.$creator['first_name'].' 
- الايدي 📂 : '.$creator['id'].'
',
		'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id,
    		]);
}
}


if (strpos($textmessage , "ضع قوانين " ) !== false ) {
if ($from_id == $admin || $from_id == $owner || strpos($modlist , "$from_id") !== false) {
$text = str_replace("ضع قوانين ","",$textmessage);
save("data/$chat_id/rules.txt","$text");
SendMessage($chat_id,"- تم حفظ القوانين الخاصةه بمجموعتك ☑️ •");
}
}

if ( strpos($textmessage , "!setrules " ) !== false )  {
if ($from_id == $admin || $from_id == $owner || strpos($modlist , "$from_id") !== false) {
$text = str_replace("!setrules ","",$textmessage);
save("data/$chat_id''.txt","$text");
SendMessage($chat_id,"- تم حفظ القوانين الخاصةه بمجموعتك ☑️ •");
}
}

if ( strpos($textmessage , "#setrules " ) !== false )  {
if ($from_id == $admin || $from_id == $owner || strpos($modlist , "$from_id") !== false) {
$text = str_replace("#setrules ","",$textmessage);
save("data/$chat_id/rules.txt","$text");
SendMessage($chat_id,"- تم حفظ القوانين الخاصةه بمجموعتك ☑️ •");
}
}

if ($textmessage == "القوانين" || $textmessage == "/rules" || $textmessage == "قوانين") {
	$gprules = file_get_contents("data/$chat_id/rules.txt");
SendMessage($chat_id,"- قوانين المجموعةه الخاصةه بك 📂 :
$gprules");
}

if ($textmessage == "/modlist" || $textmessage == "!modlist" || $textmessage == "#modlist") {
if ($from_id == $admin || $from_id == $owner || strpos($modlist , "$from_id") !== false) {
SendMessage($chat_id,"Modlist:\n$modlist");
}
}
if ($textmessage == "المدراء" || $textmessage == "!owner" || $textmessage == "#owner") {
SendMessage($chat_id,"قائمه المدراء ☑️:\n$owner");
}

if (strpos($textmessage , "/setwarn " ) !== false ) {
if ($from_id == $admin || $from_id == $owner || strpos($modlist , "$from_id") !== false && $_warn == "❌") {
$text = str_replace("/setwarn ","",$textmessage);
	if ($text >= 1 && $text <= 9) {
save("data/$chat_id/settings/warnlists.txt","$text");
SendMessage($chat_id,"تعدار خطاهای کاربر اپدیت شد");
}
	if ($text <= 0 && $text <= 10) {
SendMessage($chat_id,"تعدار خطاها باید بین ۱ تا ۹ باشد");
}
}
 }

if (strpos($textmessage , "!setwarn " ) !== false ) {
if ($from_id == $admin || $from_id == $owner || strpos($modlist , "$from_id") !== false && $_warn == "❌") {
$text = str_replace("!setwarn ","",$textmessage);
	if ($text >= 1 && $text <= 9) {
save("data/$chat_id/settings/warnlists.txt","$text");
SendMessage($chat_id,"تعدار خطاهای کاربر اپدیت شد");
}
	if ($text <= 0 && $text <= 10) {
SendMessage($chat_id,"تعدار خطاها باید بین ۱ تا ۹ باشد");
}
}
 }

if (strpos($textmessage , "#setwarn " ) !== false ) {
if ($from_id == $admin || $from_id == $owner || strpos($modlist , "$from_id") !== false && $_warn == "❌") {
$text = str_replace("#setwarn ","",$textmessage);
	if ($text >= 1 && $text <= 9) {
save("data/$chat_id/settings/warnlists.txt","$text");
SendMessage($chat_id,"تعدار خطاهای کاربر اپدیت شد");
}
	if ($text <= 0 && $text <= 10) {
SendMessage($chat_id,"تعدار خطاها باید بین ۱ تا ۹ باشد");
}
}
 }

if (strpos($textmessage , "ضع تكرار " ) !== false ) {
if ($from_id == $admin || $from_id == $owner || strpos($modlist , "$from_id") !== false && $_settings == "❌") {
$text = str_replace("ضع تكرار ","",$textmessage);
	if ($text >= 3 && $text <= 15) {
save("data/$chat_id/settings/floods.txt","$text");
SendMessage($chat_id,"- تم الحفظ ☑️ •");
}
	if ($text <= 2 && $text <= 16) {
SendMessage($chat_id,"- اختر من 3 الى 15 ☑️ •");
}
}
 }

if (strpos($textmessage , "!setflood " ) !== false ) {
if ($from_id == $admin || $from_id == $owner || strpos($modlist , "$from_id") !== false && $_settings == "❌") {
$text = str_replace("!setflood ","",$textmessage);
	if ($text >= 3 && $text <= 15) {
save("data/$chat_id/settings/floods.txt","$text");
SendMessage($chat_id,"تعدار سیل اپدیت شد");
}
	if ($text <= 2 && $text <= 16) {
SendMessage($chat_id,"- اختر من 3 الى 15 ☑️ •");
}
}
 }

if (strpos($textmessage , "#setflood " ) !== false ) {
if ($from_id == $admin || $from_id == $owner || strpos($modlist , "$from_id") !== false && $_settings == "❌") {
$text = str_replace("#setflood ","",$textmessage);
	if ($text >= 3 && $text <= 15) {
save("data/$chat_id/settings/floods.txt","$text");
SendMessage($chat_id,"- تم الحفظ ☑️ •");
}
	if ($text <= 2 && $text <= 16) {
SendMessage($chat_id,"اختر من 3 الى 15 ☑️");
}
}
 }


if (strpos($textmessage , "/setlink " ) !== false ) {
if ($from_id == $admin || $from_id == $owner ) {
$text = str_replace(" setlink ","",$textmessage);
save("data/$chat_id/gplink.txt","$text");
SendMessage($chat_id,"- تم حفظ الرابط الخاص بلمجموعه ☑️ •");
}
}

if (strpos($textmessage , "ضع رابط " ) !== false ) {
if ($from_id == $admin || $from_id == $owner ) {
$text = str_replace("ضع رابط ","",$textmessage);
save("data/$chat_id/gplink.txt","$text");
SendMessage($chat_id,"- تم حفظ الرابط الخاص بلمجموعه ☑️ •");
}
}

if (strpos($textmessage , "#setlink " ) !== false ) {
if ($from_id == $admin || $from_id == $owner ) {
$text = str_replace("#setlink ","",$textmessage);
save("data/$chat_id/gplink.txt","$text");
SendMessage($chat_id,"لینک گروه ست شد");
}
}

if($wlctext){
sendmark($chatId,"اهلاً وسهلاً : [اضغط هنا من فضلك 💎](https://telegram.me/https://t.me/joinchat/AAAAAEHD2a9Qcw-y1-5pIQ)" ,$memb);
}

if($wlctext2){
sendmark($chatId,"اهلاً وسهلاً : [اضغط هنا من فضلك 💎](https://telegram.me/https://t.me/joinchat/AAAAAEHD2a9Qcw-y1-5pIQ)" ,$memb);
}

if (strpos($textmessage , "/setwlc " ) !== false ) {
if ($from_id == $admin || $from_id == $owner ) {
$text = str_replace("/setwlc ","",$textmessage);
save("data/$chat_id/gpwlc.txt","$text");
SendMessage($chat_id,"- تم حفظ الترحيب الخاص بك ☑️ •");
}
}


if (strpos($textmessage , "ضع ترحيب " ) !== false ) {
if ($from_id == $admin || $from_id == $owner ) {
$text = str_replace("ضع ترحيب ","",$textmessage);
save("data/$chat_id/gpwlc.txt","$text");
SendMessage($chat_id,"- تم حفظ الترحيب الخاص بك ☑️ •");
}
}

if (strpos($textmessage , "#setwlc " ) !== false ) {
if ($from_id == $admin || $from_id == $owner ) {
$text = str_replace("#setwlc ","",$textmessage);
save("data/$chat_id/gpwlc.txt","$text");
SendMessage($chat_id,"متن خوش آمد گویی تغییر پیدا کرد به
$text
برای حذف کردن دستور /delwlc را بفرستید");
}
}

if($textmessage=="/delwlc" || $textmessage=="مسح الترحيب" || $textmessage=="#delwlc"  ){
if ($from_id == $admin || $from_id == $owner ) {
save("data/$chat_id/gpwlc.txt","");
makereq('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"- تم حذف ترحيب الخاص بالمجموعه ☑️ •",
'reply_to_message_id'=>$update->message->message_id,
]);
}
}

if (strpos($textmessage , "/setbye " ) !== false ) {
if ($from_id == $admin || $from_id == $owner ) {
$text = str_replace("/setbye ","",$textmessage);
save("data/$chat_id/gpbye.txt","$text");
SendMessage($chat_id,"- تم حفظ التوديع الخاص بالمجموعه ☑️ •");
}
}

if (strpos($textmessage , "ضع توديع " ) !== false ) {
if ($from_id == $admin || $from_id == $owner ) {
$text = str_replace("ضع توديع ","",$textmessage);
save("data/$chat_id/gpbye.txt","$text");
SendMessage($chat_id,"- تم حفظ التوديع الخاص بالمجموعه ☑️ •");
}
}

if (strpos($textmessage , "#setbye " ) !== false ) {
if ($from_id == $admin || $from_id == $owner ) {
$text = str_replace("#setbye ","",$textmessage);
save("data/$chat_id/gpbye.txt","$text");
SendMessage($chat_id,"متن خداحافظی تغییر پیدا کرد به
$text
برای حذف کردن دستور /delbye را بفرستید");
}
}

if($textmessage=="/delbye" || $textmessage=="مسح التوديع" || $textmessage=="#delbye"  ){
if ($from_id == $admin || $from_id == $owner ) {
save("data/$chat_id/gpbye.txt","");
makereq('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"- تم مسح التوديع ☑️ •",
'reply_to_message_id'=>$update->message->message_id,
]);
}
}

if($textmessage=="/link" || $textmessage=="الرابط" || $textmessage=="#link"  ){
	$gplink = file_get_contents("data/$chat_id/gplink.txt");
makereq('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"- `رابط المجموعةه ↘️` -
$gplink",
       	'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
]);
}
if (strpos($textmessage , "ايديي ") !== false) {
$text = str_replace("ايديي ","",$textmessage);
SendMessage($chat_id,"- تم الارسال الى الخاص - ☑️");
makereq('sendmessage',[
'chat_id'=>$admin,
'text'=>"هاهههه: $text",
       	'parse_mode'=>'HTML',
]);
makereq('sendmessage',[
'chat_id'=>$admin,
'text'=>"اسمك: $name
معرفك: @$username
ايديك: $from_id",
       	'parse_mode'=>'HTML',
]);
}


		if ( strpos($textmessage , 'حظر ') !== false  ) {
						if ($from_id == $admin || $from_id == $owner || strpos($modlist , "$from_id") !== false  && $_ban2 == "❌"){
			$text = str_replace("حظر ","",$textmessage);
									if ($text != $admin && $text != $owner && $text != $modlist ){
			makereq('kickChatMember',[
            		'chat_id'=>$update->message->chat->id,
            		'user_id'=>$text
        		]);
			$myfile2 = fopen("data/$chat_id/banlist/list.txt", "a") or die("Unable to open file!");	
			fwrite($myfile2, "$text\n");
			fclose($myfile2);
			makereq('sendMessage',[
            		'chat_id'=>$update->message->chat->id,
            		'text'=>'- العضو تم حظره من المجموعه ☑️ •',
            		'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
        		]);
		}
		}
		}

		if ( strpos($textmessage , 'طرد ') !== false ) {
    		if ($from_id == $admin || $from_id == $owner || strpos($modlist , "$from_id") !== false  && $_kick2 == "❌" ){
			$text = str_replace("طرد ","",$textmessage);
									if ($text != $admin && $text != "@" && $text != $owner && $text != $modlist ){
					makereq('kickChatMember',[
            		'chat_id'=>$update->message->chat->id,
            		'user_id'=>$text
        		]);
			makereq('unbanChatMember',[
            		'chat_id'=>$update->message->chat->id,
            		'user_id'=>$text
        		]);
			makereq('sendMessage',[
            		'chat_id'=>$update->message->chat->id,
            		'text'=>'- تم طرد العضو من المجموعه ☑️ •',
            		'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
        		]);
		}
									if ($text != $admin && strpos($text , "@") !== false && $text != $owner && $text != $modlist ){
					makereq('kickChatMember',[
            		'chat_id'=>$update->message->chat->id,
            		'user_id'=>$text->id
        		]);
			makereq('unbanChatMember',[
            		'chat_id'=>$update->message->chat->id,
            		'user_id'=>$text->id
        		]);
			makereq('sendMessage',[
            		'chat_id'=>$update->message->chat->id,
            		'text'=>'- تم طرد العضو من المجموعه ☑️ •',
            		'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
        		]);
		}
}
	}
				if ( strpos($textmessage , 'الغاء حظر ') !== false  ) {
		if ($from_id == $admin || $from_id == $owner || strpos($modlist , "$from_id") !== false  && $_unban2 == "❌"){
					$text = str_replace("الغاء حظر ","",$textmessage);
							if ($text != $admin && $text != $owner && $text != $modlist ){
								makereq('unbanChatMember',[
            		'chat_id'=>$update->message->chat->id,
            		'user_id'=>$text
        		]);
					$newlist = str_replace("$text\n","",$banlist);
			save("data/$chat_id/banlist/list.txt",$newlist);
			makereq('sendMessage',[
            		'chat_id'=>$update->message->chat->id,
            		'text'=>'- تم الغاء حظر العضو من المجموعه ☑️ •',
            		'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
        	]);
		}
	}
}

if (strpos($textmessage , "منع" ) !== false ) {
if ($from_id == $admin || $from_id == $owner || strpos($modlist , "$from_id") !== false) {
$text = str_replace("منع ","",$textmessage);
$myfile2 = fopen("data/$chat_id/settings/filterword.txt", 'a') or die("Unable to open file!");	
fwrite($myfile2, "$text \n");
fclose($myfile2);
SendMessage($chat_id,"- الكلمه $text تم اضافتها الى قائمه المنع ☑️ •");
}
}

if (strpos($textmessage , "/addfilter" ) !== false ) {
if ($from_id == $admin || $from_id == $owner || strpos($modlist , "$from_id") !== false) {
$text = str_replace("/addfilter ","",$textmessage);
$myfile2 = fopen("data/$chat_id/settings/filterword.txt", 'a') or die("Unable to open file!");	
fwrite($myfile2, "$text \n");
fclose($myfile2);
SendMessage($chat_id,"- الكلمه $text تم اضافتها الى قائمه المنع ☑️ •");
}
}

if (strpos($textmessage , "#addfilter" ) !== false ) {
if ($from_id == $admin || $from_id == $owner || strpos($modlist , "$from_id") !== false) {
$text = str_replace("#addfilter ","",$textmessage);
$myfile2 = fopen("data/$chat_id/settings/filterword.txt", 'a') or die("Unable to open file!");	
fwrite($myfile2, "$text \n");
fclose($myfile2);
SendMessage($chat_id,"$text added to FilterList");
}
}

if (strpos($textmessage , "الغاء منع" ) !== false ) {
if ($from_id == $admin || $from_id == $owner || strpos($modlist , "$from_id") !== false) {
$text = str_replace("الغاء منع ","",$textmessage);
			$newlist = str_replace("$text\n","",$filterlist);
			save("data/$chat_id/settings/filterword.txt",$newlist);
SendMessage($chat_id,"- الكلمه $text تم الغاء منعها ☑️ •");
}
}

if (strpos($textmessage , "/delfilter" ) !== false ) {
if ($from_id == $admin || $from_id == $owner || strpos($modlist , "$from_id") !== false) {
$text = str_replace("/delfilter ","",$textmessage);
			$newlist = str_replace("$text\n","",$filterlist);
			save("data/$chat_id/settings/filterword.txt",$newlist);
SendMessage($chat_id,"- الكلمه $text تم الغاء منعها ☑️ •");
}
}

if (strpos($textmessage , "#delfilter" ) !== false ) {
if ($from_id == $admin || $from_id == $owner || strpos($modlist , "$from_id") !== false) {
$text = str_replace("#delfilter ","",$textmessage);
			$newlist = str_replace("$text\n","",$filterlist);
			save("data/$chat_id/settings/filterword.txt",$newlist);
SendMessage($chat_id,"$text deleted to FilterList");
}
}

if($textmessage=="قائمه المنع" ){
makereq('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"الكلمات الممنوعه هي ☑️ :
$filterlist",
       	'parse_mode'=>'HTML',
       	'reply_to_message_id'=>$update->message->message_id,
       	'disable_web_page_preview'=>true
]);
}
	
	if ($reply != null && $from_id == $admin || $reply != null && $from_id == $owner) {
		if ($textmessage == '/del' || $textmessage == 'مسح' || $textmessage == '#del' ) {
			makereq('deletemessage',[
                    'chat_id'=>$update->message->chat->id,
            				'message_id'=>$update->message->reply_to_message->message_id
				        		]);
			makereq('deletemessage',[
                    'chat_id'=>$update->message->chat->id,
            				'message_id'=>$update->message->message_id
				        		]);
				}
		if ($textmessage == '/ban' || $textmessage == 'حظر' || $textmessage == '#ban' ) {
									if ($reply != $admin && $reply != $owner && $reply != $modlist ){
			makereq('kickChatMember',[
            		'chat_id'=>$update->message->chat->id,
            		'user_id'=>$reply
        		]);
			$myfile2 = fopen("data/$chat_id/banlist/list.txt", "a") or die("Unable to open file!");	
			fwrite($myfile2, "$reply\n");
			fclose($myfile2);
			makereq('sendMessage',[
            		'chat_id'=>$update->message->chat->id,
            		'text'=>'- العضو تم حظره من المجموعه ☑️ •',
            		'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
        		]);
		}
		}
				if ($textmessage == '/kick' || $textmessage == 'طرد' || $textmessage == '#kick') {
						if ($reply != $admin && $reply != $owner && $reply != $modlist ){
					makereq('kickChatMember',[
            		'chat_id'=>$update->message->chat->id,
            		'user_id'=>$reply
        		]);
			makereq('unbanChatMember',[
            		'chat_id'=>$update->message->chat->id,
            		'user_id'=>$reply
        		]);
			makereq('sendMessage',[
            		'chat_id'=>$update->message->chat->id,
            		'text'=>'- العضو تم طرده من المجموعه ☑️ •',
            		'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
        		]);
		}
				}
				if ($textmessage == '/unban' || $textmessage == 'الغاء حظر' || $textmessage == '#unban') {
											if ($reply != $admin && $reply != $owner && $reply != $modlist ){
								makereq('unbanChatMember',[
            		'chat_id'=>$update->message->chat->id,
            		'user_id'=>$reply
        		]);
					$newlist = str_replace("$reply\n","",$banlist);
			save("data/$chat_id/banlist/list.txt",$newlist);
			makereq('sendMessage',[
            		'chat_id'=>$update->message->chat->id,
            		'text'=>'- العضو تم الغاء حظره ☑️ •',
            		'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
        	]);
		}
	}
			if ($textmessage == '/promote' || $textmessage == 'رفع ادمن' || $textmessage == '#promote') {
			$myfile2 = fopen("data/$chat_id/modlist.txt", "a") or die("Unable to open file!");	
			fwrite($myfile2, "$reply\n");
			fclose($myfile2);
									if( $replyusername != "" ){
			SendMessage2($chat_id,"- العضو @$replyusername تم رفعه ادمن ☑️ •");
			}else{
			SendMessage($chat_id,"- العضو $reply تم رفعه ادمن ☑️ •");
		}
	}
				if ($textmessage == '/setowner' || $textmessage == 'رفع مدير' || $textmessage == '#setowner') {
			save("data/$chat_id/owner.txt", "$reply");
			SendMessage($chat_id,"- العضو $reply تم رفعه مدير ☑️ •");
		}
		if ($textmessage == '/demote' || $textmessage == 'تنزيل ادمن' || $textmessage == '#demote') {
			$newlist = str_replace("$reply\n","",$modlist);
			save("data/$chat_id/modlist.txt",$newlist);
								if( $replyusername != "" ){
			SendMessage2($chat_id,"- العضو @$replyusername تم تنزيله من الادمنيه ☑️ •");
			}else{
			SendMessage($chat_id,"- العضو $reply تم تنزيله من الادمنيه ☑️ •");
		}
		}

						if ($textmessage == '/muteuser' || $textmessage == 'كتم' || $textmessage == '#muteuser') {
								if ($reply != $admin && $reply != $owner && $reply != $modlist ){
			$myfile2 = fopen("data/$chat_id/muteuserlist.txt", "a") or die("Unable to open file!");	
			fwrite($myfile2, "$reply\n");
			fclose($myfile2);
					if( $replyusername != "" ){
					makereq('sendMessage',[
            		'chat_id'=>$update->message->chat->id,
            		'text'=>'- العضو '.$reply.'  تم كتمه ⚠️ •',
            		'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
        		]);
		}else{
			makereq('sendMessage',[
            		'chat_id'=>$update->message->chat->id,
            		'text'=>'- العضو '.$reply.'  تم كتمه ⚠️ •',
            		'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
        		]);
		}
		}
				}
						if ($textmessage == '/unmuteuser' || $textmessage == 'الغاء كتم' || $textmessage == '#unmuteuser') {
								if ($reply != $admin && $reply != $owner && $reply != $modlist ){
	$muteuserlist == str_replace("data/$chat_id/muteuserlist.txt");
$newlist = str_replace("$reply\n","",$muteuserlist);
save("data/$chat_id/muteuserlist.txt",$newlist);
								if( $replyusername != "" ){
			makereq('sendMessage',[
            		'chat_id'=>$update->message->chat->id,
            		'text'=>'- العضو  @'.$replyusername.'  تم الغاء كتمه ⚠️ •',
            		'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
        		]);
			}else{
			makereq('sendMessage',[
            		'chat_id'=>$update->message->chat->id,
            		'text'=>'- العضو  @'.$replyusername.'  تم الغاء كتمه ⚠️ •',
            		'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
        		]);
		}
}
		}
					if ($textmessage == '/warn' || $textmessage == 'تحذير' || $textmessage == '#warn') {
								if ($reply != $admin && $reply != $owner && $reply != $modlist ){
												if (!file_exists("data/$chat_id/member/".$reply."3.txt")) {
			save("data/$chat_id/member/".$reply."3.txt","");
}
			$ekhtart =0;
				$fp = fopen( "data/$chat_id/member/".$reply."3.txt", 'r');
	while( !feof( $fp)) {
    		fgets( $fp);
    		$ekhtart ++;
	}
	fclose( $fp);
			$myfile2 = fopen("data/$chat_id/member/".$reply."3.txt",'a') or die("Unable to open file!");	
fwrite($myfile2, "$ekhtart\n");
fclose($myfile2);
					if( $replyusername != "" ){
					makereq('sendMessage',[
            		'chat_id'=>$update->message->chat->id,
            		'text'=>'- العضو @'.$replyusername.' تم تحذيره ⚠️ •',
            		'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
        		]);
		}else{
			makereq('sendMessage',[
            		'chat_id'=>$update->message->chat->id,
            		'text'=>'- العضو '.$reply.' تم تحذيره ⚠️ •',
            		'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
        		]);
		}
		}
				}
						if ($textmessage == '/unwarn' || $textmessage == 'الغاء تحذير' || $textmessage == '#unwarn') {
								if ($reply != $admin && $reply != $owner && $reply != $modlist ){
												if (!file_exists("data/$chat_id/member/".$reply."3.txt")) {
			save("data/$chat_id/member/".$reply."3.txt","0");
}
			$ekhtart =-1;
				$fp = fopen( "data/$chat_id/member/".$reply."3.txt", 'r');
	while( !feof( $fp)) {
    		fgets( $fp);
    		$ekhtart ++;
	}
	fclose( $fp);
if ($ekhtart >= 1) {
	$ekhtarlist == str_replace("data/$chat_id/member/".$reply."3.txt");
$newlist = str_replace("$ekhtart\n","",$ekhtarlist);
save("data/$chat_id/member/".$reply."3.txt",$newlist);
								if( $replyusername != "" ){
			makereq('sendMessage',[
            		'chat_id'=>$update->message->chat->id,
            		'text'=>'- العضو @'.$replyusername.' تم الغاء تحذيره ⚠️ •',
            		'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
        		]);
			}else{
			makereq('sendMessage',[
            		'chat_id'=>$update->message->chat->id,
            		'text'=>'- العضو  '.$reply.'  تم مسح التحذيرات ⚠️ •',
            		'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
        		]);
		}
}
	if ($ekhtart == 0) {
	if( $replyusername != "" ){
			makereq('sendMessage',[
            		'chat_id'=>$update->message->chat->id,
            		'text'=>'- العضو @'.$replyusername.' تم الغاء تحذيره ⚠️ •',
            		'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
        		]);
			}else{
			makereq('sendMessage',[
            		'chat_id'=>$update->message->chat->id,
            		'text'=>'حدث خطا',
            		'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
        		]);
		}
								}
				}
			}
						if ($textmessage == '/setwhitelist' || $textmessage == 'رفع عضو مميز' || $textmessage == '#setwhitelist') {
								if ($reply != $admin && $reply != $owner && $reply != $modlist ){
													if (!file_exists("data/$chat_id/whitelist")) {
			mkdir("data/$chat_id/whitelist");
}
												if (!file_exists("data/$chat_id/whitelist/list.txt")) {
			save("data/$chat_id/whitelist/list.txt");
}
			$myfile2 = fopen("data/$chat_id/whitelist/list.txt", "a") or die("Unable to open file!");	
			fwrite($myfile2, "$reply\n");
			fclose($myfile2);
								if( $replyusername != "" ){
					makereq('sendMessage',[
            		'chat_id'=>$update->message->chat->id,
            		'text'=>'- العضو @'.$replyusername.' تم رفعه عضو مميز ⚠️ •',
            		'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
        		]);
		}else{
			makereq('sendMessage',[
            		'chat_id'=>$update->message->chat->id,
            		'text'=>'- العضو  '.$reply.'  تم رفعه عضو مميز ⚠️ •',
            		'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
        		]);
		}
				}
						}
						if ($textmessage == '/delwhitelist' || $textmessage == 'تنزيل عضو مميز' || $textmessage == '#delwhitelist') {
								if ($reply != $admin && $reply != $owner && $reply != $modlist ){
													if (!file_exists("data/$chat_id/whitelist")) {
			mkdir("data/$chat_id/whitelist");
}
												if (!file_exists("data/$chat_id/whitelist/list.txt")) {
			save("data/$chat_id/whitelist/list.txt");
}
	$newlist = str_replace("$reply\n","",$whitelist);
			save("data/$chat_id/whitelist/list.txt",$newlist);
											if( $replyusername != "" ){
					makereq('sendMessage',[
            		'chat_id'=>$update->message->chat->id,
            		'text'=>'- العضو @'.$replyusername.' تم تنزيله ⚠️ •',
            		'disable_web_page_preview'=>true
        		]);
		}else{
			makereq('sendMessage',[
            		'chat_id'=>$update->message->chat->id,
            		'text'=>'- العضو  '.$reply.' تم تنزيله ⚠️ •',
            		'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
        		]);
		}
				}
						}
		if ($textmessage == '/info' || $textmessage == 'معلومات' || $textmessage == '#info') {
			if (!file_exists("data/$chat_id/member/".$reply."3.txt")) {
			save("data/$chat_id/member/".$reply."3.txt","");
}
			$ekhtart3 =-1;
				$fp = fopen( "data/$chat_id/member/".$reply."3.txt", 'r');
	while( !feof( $fp)) {
    		fgets( $fp);
    		$ekhtart3 ++;
	}
makereq('sendMessage',[
  'chat_id' => $update->message->chat->id,
  "text" => 'معلومات العضو هي

الاسم: '.$replyname.'

المعرف: <a href="t.me/'.$replyusername.'">@'.$replyusername.'</a>

الايدي: '.$reply.' ',
            	'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
			]);
	
	}
	}
		
		
		
	if ($reply != null && strpos($modlist , "$from_id") !== false) {
				if ($textmessage == '/del' || $textmessage == 'مسح' || $textmessage == '#del' ) {
			makereq('deletemessage',[
                    'chat_id'=>$update->message->chat->id,
            				'message_id'=>$update->message->reply_to_message->message_id
				        		]);
			makereq('deletemessage',[
                    'chat_id'=>$update->message->chat->id,
            				'message_id'=>$update->message->message_id
				        		]);
				}
		if ($textmessage == '/ban' && $_ban3 == "❌"|| $textmessage == 'حظر' && $_ban3 == "❌" || $textmessage == '#ban' && $_ban3 == "❌") {
			makereq('kickChatMember',[
            		'chat_id'=>$update->message->chat->id,
            		'user_id'=>$reply
        		]);
			$myfile2 = fopen("data/$chat_id/banlist/list.txt", "a") or die("Unable to open file!");	
			fwrite($myfile2, "$reply\n");
			fclose($myfile2);
			makereq('sendMessage',[
            		'chat_id'=>$update->message->chat->id,
            		'text'=>'- تم حظر العضو من المجموعةه⚠️ •',
            		'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
        		]);
		}
				if ($textmessage == '/kick' && $_kick3 == "❌"|| $textmessage == 'طرد' && $_kick3 == "❌" || $textmessage == '#kick' && $_kick3 == "❌") {
						if ($reply != $admin && $reply3 != $owner3 && $reply != $modlist3 ){
					makereq('kickChatMember',[
            		'chat_id'=>$update->message->chat->id,
            		'user_id'=>$reply
        		]);
			makereq('unbanChatMember',[
            		'chat_id'=>$update->message->chat->id,
            		'user_id'=>$reply
        		]);
			makereq('sendMessage',[
            		'chat_id'=>$update->message->chat->id,
            		'text'=>'- تم طرد العضو من المجموعةه ⚠️ •',
            		'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
        		]);
		}
				}
			if ($textmessage == '/unban' && $_unban3 == "❌" || $textmessage == 'الغاء حظر' && $_unban3 == "❌" || $textmessage == '#unban' && $_unban3 == "❌") {
											if ($reply != $admin && $reply != $owner3 && $reply != $modlist3 ){
								makereq('unbanChatMember',[
            		'chat_id'=>$update->message->chat->id,
            		'user_id'=>$reply
        		]);
					$newlist = str_replace("$reply\n","",$banlist);
			save("data/$chat_id/banlist/list.txt",$newlist);
			makereq('sendMessage',[
            		'chat_id'=>$update->message->chat->id,
            		'text'=>'- تم الغاء حظر العضو من المجموعةه ⚠️ •',
            		'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
        	]);
		}
	}
		
								if ($textmessage == '/muteuser' || $textmessage == 'كتم' || $textmessage == '#muteuser') {
								if ($reply != $admin && $reply != $owner && $reply != $modlist ){
			$myfile2 = fopen("data/$chat_id/muteuserlist.txt", "a") or die("Unable to open file!");	
			fwrite($myfile2, "$reply\n");
			fclose($myfile2);
					if( $replyusername != "" ){
					makereq('sendMessage',[
            		'chat_id'=>$update->message->chat->id,
            		'text'=>'- العضو @'.$replyusername.' تم كتمه ⚠️ •',
            		'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
        		]);
		}else{
			makereq('sendMessage',[
            		'chat_id'=>$update->message->chat->id,
            		'text'=>'- العضو  '.$reply.'  تم كتمه ⚠️ •',
            		'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
        		]);
		}
		}
				}
						if ($textmessage == '/unmuteuser' && $_muteuser3 == "❌" || $textmessage == 'الغاء كتم' && $_muteuser3 == "❌" || $textmessage == '#unmuteuser' && $_muteuser3 == "❌") {
								if ($reply != $admin && $reply != $owner && $reply != $modlist ){
	$muteuserlist == str_replace("data/$chat_id/muteuserlist.txt");
$newlist = str_replace("$reply\n","",$muteuserlist);
save("data/$chat_id/muteuserlist.txt",$newlist);
								if( $replyusername != "" ){
			makereq('sendMessage',[
            		'chat_id'=>$update->message->chat->id,
            		'text'=>'- العضو @'.$replyusername.'  تم الغاء كتمه ⚠️ •',
            		'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
        		]);
			}else{
			makereq('sendMessage',[
            		'chat_id'=>$update->message->chat->id,
            		'text'=>'- العضو  '.$reply.'  تم الغاء كتمه ⚠️ •',
            		'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
        		]);
		}
}
		}
		
						if ($textmessage == '/warn' && $_warn3 == "❌" || $textmessage == 'تحذير' && $_warn3 == "❌" || $textmessage == '#warn' && $_warn3 == "❌") {
								if ($reply != $admin && $reply != $owner && $reply != $modlist ){
												if (!file_exists("data/$chat_id/member/".$reply."3.txt")) {
			save("data/$chat_id/member/".$reply."3.txt","");
}
			$ekhtart =0;
				$fp = fopen( "data/$chat_id/member/".$reply."3.txt", 'r');
	while( !feof( $fp)) {
    		fgets( $fp);
    		$ekhtart ++;
	}
	fclose( $fp);
			$myfile2 = fopen("data/$chat_id/member/".$reply."3.txt",'a') or die("Unable to open file!");	
fwrite($myfile2, "$ekhtart\n");
fclose($myfile2);
					if( $replyusername != "" ){
					makereq('sendMessage',[
            		'chat_id'=>$update->message->chat->id,
            		'text'=>'- العضو @'.$replyusername.' تم الغاء تحذيره ⚠️ •',
            	'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
        		]);
		}else{
			makereq('sendMessage',[
            		'chat_id'=>$update->message->chat->id,
            		'text'=>'- العضو  '.$reply.' تم تحذيره ⚠️ •',
            		'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
        		]);
		}
		}
				}
						if ($textmessage == '/unwarn' && $_warn3 == "❌" || $textmessage == 'الغاء تحذير' && $_warn3 == "❌" || $textmessage == '#unwarn' && $_warn3 == "❌") {
								if ($reply != $admin && $reply != $owner && $reply != $modlist ){
												if (!file_exists("data/$chat_id/member/".$reply."3.txt")) {
			save("data/$chat_id/member/".$reply."3.txt","0");
}
			$ekhtart =-1;
				$fp = fopen( "data/$chat_id/member/".$reply."3.txt", 'r');
	while( !feof( $fp)) {
    		fgets( $fp);
    		$ekhtart ++;
	}
	fclose( $fp);
if ($ekhtart >= 1) {
	$ekhtarlist == str_replace("data/$chat_id/member/".$reply."3.txt");
$newlist = str_replace("$ekhtart\n","",$ekhtarlist);
save("data/$chat_id/member/".$reply."3.txt",$newlist);
								if( $replyusername != "" ){
			makereq('sendMessage',[
            		'chat_id'=>$update->message->chat->id,
            		'text'=>'- العضو @'.$replyusername.' تم الغاء تحذيره ⚠️ •',
            		'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
        		]);
			}else{
			makereq('sendMessage',[
            		'chat_id'=>$update->message->chat->id,
            		'text'=>'- العضو  '.$reply.' تم مسح تحذيراته ⚠️ •',
            		'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
        		]);
		}
}
	if ($ekhtart == 0) {
	if( $replyusername != "" ){
			makereq('sendMessage',[
            		'chat_id'=>$update->message->chat->id,
            		'text'=>'- العضو @'.$replyusername.' تم الغاء تحذيره ⚠️ •',
            		'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
        		]);
			}else{
			makereq('sendMessage',[
            		'chat_id'=>$update->message->chat->id,
            		'text'=>'هناك خطا',
            		'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
        		]);
		}
								}
				}
			}
		
		if ($textmessage == '/info' || $textmessage == 'معلومات' || $textmessage == '#info') {
			if (!file_exists("data/$chat_id/member/".$reply."3.txt")) {
			save("data/$chat_id/member/".$reply."3.txt","");
}
			$ekhtart3 =-1;
				$fp = fopen( "data/$chat_id/member/".$reply."3.txt", 'r');
	while( !feof( $fp)) {
    		fgets( $fp);
    		$ekhtart3 ++;
	}
makereq('sendMessage',[
  'chat_id' => $update->message->chat->id,
  "text" => 'معلومات العضو هي

الاسم: '.$replyname.'

المعرف: <a href="t.me/'.$replyusername.'">@'.$replyusername.'</a>

الايدي: '.$reply.' ',
            	'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id
			]);
	
	}
		
	}


if(isset($update->inline_query)){
	$time = file_get_contents("http://irapi.ir/time");
	$fatime = $time->result->FAtime;
	$fadate = $time->FAdate;
	$fadate = $time->ENdate;
	$from_id = $update->inline_query->from->id;
  $lname = $update->inline_query->from->last_name;
	$fname = $update->inline_query->from->first_name;
  $username = $update->inline_query->from->username;
  $inline_id = $update->inline_query->id;
  $inline_m = $update->inline_query->query;
	$callback_data = $update->callback_query->data;
  $callback_id = $update->callback_query->id;	
  makereq('answerInlineQuery',[
    'inline_query_id'=>$inline_id,
    'results'=>json_encode([
     [
        'type'=>'article',
        'id'=>base64_encode(4),
        'title'=>'- معلومات حسابك 📡 -',
        'input_message_content'=>[
          'message_text'=>'<b>- اهلا بك عزيزي معلومات حسابك هي ↘️ -</b>

- اسمك<b> 📬</b> : '.$fname.' '.$lname.'
- معرفك<b> ☑️</b> : <a href="t.me/'.$username.'">@'.$username.'</a>
- ايديك<b> ⚠️</b> : '.$from_id.'
'
		,
          'parse_mode'=>'HTML'
        ]
      ],[
        'type'=>'article',
        'id'=>base64_encode(1),
        'title'=>'Bold '.($inline_m),
        'input_message_content'=>[
          'message_text'=>'<b>'.($inline_m).'</b>',
          'parse_mode'=>'HTML'
        ]
      ],
      [
        'type'=>'article',
        'id'=>base64_encode(2),
        'title'=>'Italic '.($inline_m),
        'input_message_content'=>[
          'message_text'=>'<i>'.($inline_m).'</i>',
          'parse_mode'=>'HTML'
        ]
      ],
      [
        'type'=>'article',
        'id'=>base64_encode(3),
        'title'=>'Code '.($inline_m),
        'input_message_content'=>[
          'message_text'=>'<code>'.($inline_m).'</code>',
          'parse_mode'=>'HTML'
        ]
      ]])
  ]);

}

?>