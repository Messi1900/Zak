<?php
error_reporting(0);
$host=$_SERVER['HTTP_HOST'].$_SERVER['PHP_SELF'];
$usermn = "LEO_X74";
$userbot = "Leott21bot";
$admiin = "27274549";
define("API_KEY","6629869721:AAEMcRi2MA4Ti-TNmoptXL9TXYzDW7-T9kM");
function bot($method,$datas=[]){
    $url = "https://api.telegram.org/bot".API_KEY."/".$method;
$ch = curl_init();
    curl_setopt($ch,CURLOPT_URL,$url);
    curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);
    curl_setopt($ch,CURLOPT_POSTFIELDS,$datas);
    $res = curl_exec($ch);
    if(curl_error($ch)){
        var_dump(curl_error($ch));
    }else{
        return json_decode($res);
    }
}
$update = json_decode(file_get_contents('php://input'));
$message = $update->message;
$from_id = $message->from->id;
$chat_id = $message->chat->id;
$text = $message->text;
$message_id = $message->message_id;
$message_id = $update->message->message_id;
$first_name = $message->from->first_name;
$username = $message->from->username;
//\\
$data = $update->callback_query->data;
$chat_id2 = $update->callback_query->message->chat->id;
$message_id2 = $update->callback_query->message->message_id;
$chat= $update->channel_post->chat->id;
$name = $message->from->first_name;
$name_admen = $update->name_admen; 
$text1 = $update->channel_post->text;
$from_id = $update->channel_post->from->id;
$id_admen = $update->chat_member->from->id; 
$name_admen = $update->chat_member->from->first_name;
$user_admen = $update->chat_member->from->username;
$ban = $update->chat_member->new_chat_member->status;
$chatban = $update->chat_member->chat->id;
$ban_id = $update->chat_member->old_chat_member->user->id; 
$ban_name = $update->chat_member->old_chat_member->user->first_name;
$ban_user = $update->chat_member->old_chat_member->user->username;
$tt = json_decode(file_get_contents('php://input'))->my_chat_member->old_chat_member->can_promote_members; 
$ccc = json_decode(file_get_contents('php://input'))->my_chat_member->chat->id;
$admen = json_decode(file_get_contents('php://input'))->my_chat_member->from->id;
$ba = json_decode(file_get_contents('php://input'))->my_chat_member->new_chat_member->can_promote_members;
$viruss = json_encode(['message', 'edited_message', 'channel_post', 'edited_channel_post', 'inline_query', 'chosen_inline_result', 'callback_query', 'shipping_query', 'pre_checkout_query', 'poll', 'poll_answer', 'my_chat_member', 'chat_member']); file_get_contents("https://api.telegram.org/bot$token/setwebhook?max_connections=100&allowed_updates=" . $viruss . "&drop_pending_updates=true&url=https://$host");
//\\
$update->channel_post;
$chid = $update->channel_post->chat->id;
$chtext = $update->channel_post->text;
$messageid= $update->channel_post->message_id;
$document = $update->channel_post->document;
$sticker= $update->channel_post->sticker;
$photo= $update->channel_post->photo;
$video= $update->channel_post->video;
$forward= $update->channel_post->forward_from_chat;
$contact= $update->channel_post->contact;
$audio= $update->channel_post->audio;
//\\
$documents = "المتحركة";
$stickers = "الملصقات";
$photos = "الصور";
$videos = "الفيديو";
$forwards = "التوجيه";
$contacts = "المواقع";
$audios = "الصوت";
$links = "الروابط";
$usernames = "المعرفات";
//\\
mkdir ("data");
//\\
$setnamebot = file_get_contents("setname.txt");
$namebot = file_get_contents("namebot.txt");
//\\
$message = $update->message;
$chat_id = $message->chat->id;
$text = $message->text;
$from_id = $message->from->id;
$data = $update->callback_query->data;
$chat_id2 = $update->callback_query->message->chat->id;
$message_id2 =  $update->callback_query->message->message_id;
$from_id2 = $update->callback_query->from->id;
$name = $message->from->first_name;
$username = $message->from->username;
$from_id = $message->from->id;
$photo = $message->photo;
$video = $message->video;
$sticmkar = $message->sticmkar;
$file = $message->document;
$audio = $message->audio;
$voice = $message->voice;
$caption = $message->caption;
$photo_id = $message->photo[back]->file_id;
$video_id= $message->video->file_id;
$sticmkar_id = $message->sticmkar->file_id;
$file_id = $message->document->file_id;
$music_id = $message->audio->file_id;
$forward = $message->forward_from_chat;
$hmo = json_decode(file_get_contents("data.json"),1);
$hmode = json_decode(file_get_contents("hmo.json"),1);
//\\

$all = count($hmo['id'])-1;
if($message && !in_array($from_id,$hmo['id'])){
file_put_contents("data.json");
$hmo['id'][] = "$from_id";
file_put_contents("data.json",json_encode($hmo));
}
$a1 = $admiin;
$admin = array(27274549,$a1,$hmo['admin']);
$chhhhh = $hmo['inlinech1'];
$chhh = $hmo['inlinech2'];
$ch1 = file_get_contents("https://api.telegram.org/bot".API_KEY."/getChatMember?chat_id=".$hmo['ch1']."&user_id=".$from_id);
$getch1 = json_decode(file_get_contents("http://api.telegram.org/bot$token/getChat?chat_id=".$hmo['inlinech1']))->result;
$getch2 = json_decode(file_get_contents("http://api.telegram.org/bot$token/getChat?chat_id=".$hmo['inlinech2']))->result;
$Namech1 = $getch1->title;
$Namech2 = $getch2->title;
$telegram = $chhhhh;
$telegram2 = $telegram;
$telegram3 = str_replace("@","",$telegram2);
$telegram4 = $chhh;
$telegram5 = $telegram4;
$telegram6 = str_replace("@","",$telegram5);
#////////////{hmo}////////////#
if($message && (strpos($ch1,'"status":"left"') or strpos($ch1,'"Bad Request: USER_ID_INVALID"') or strpos($ch1,'"status":"kicmkad"'))!== false){
bot('sendMessage', [
'chat_id'=>$chat_id,
'text'=>'• عذرا عزيزي عليك الاشتراك بقناة البوت ليتم تشغيل 
'.$hmo['ch1'],
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"$Namech1" ,'url'=>"t.me//$telegram3"],['text'=>"$Namech2" ,'url'=>"t.me//$telegram6"]],
]])
]);return false;
}
#////////////{hmo}////////////#
$ch2 = file_get_contents("https://api.telegram.org/bot".API_KEY."/getChatMember?chat_id=".$hmo['ch2']."&user_id=".$from_id);
if($message && (strpos($ch2,'"status":"left"') or strpos($ch2,'"Bad Request: USER_ID_INVALID"') or strpos($ch2,'"status":"kicmkad"'))!== false){
bot('sendMessage', [
'chat_id'=>$chat_id,
'text'=>'• عذرا عزيزي عليك الاشتراك بقناة البوت ليتم تشغيل 
'.$hmo['ch2'],
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"$Namech1" ,'url'=>"t.me//$telegram3"],['text'=>"$Namech2" ,'url'=>"t.me//$telegram6"]],
]])
]);return false;
}
$bot = $hmo['bot'];
$o1 = $hmo['o1'];
$o2 = $hmo['o2'];
#////////////{hmo}////////////#
if($text == "/start" and in_array($from_id,$admin)){
bot("sendmessage",[
"chat_id"=>$chat_id,
"text"=>"• اهلا بك في لوحه الأدمن الخاصه بالبوت 🤖

- يمكنك التحكم في البوت الخاص بك من هنا
~~~~~~~~~~~~~~~~~ 
",
 'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>'true',
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• عمل البوت : '.$i4.' •' ,'callback_data'=>"bot"],['text'=>'اشعارات الدخول '.$o1.'' ,'callback_data'=>"o1"]],
[['text'=>'اشعارات الاستخدام '.$o2.'','callback_data'=>"o2"]],
[['text'=>"• الاشتراك •" ,'callback_data'=>"ch"],['text'=>"• رفع ادمن •" ,'callback_data'=>"3"]],
[['text'=>"• اذاعة •" ,'callback_data'=>"1"],['text'=>"• الاحصائيات •" ,'callback_data'=>"2"]],
]])
]);
$hmo['data'] = "stop";
file_put_contents("data.json",json_encode($hmo));
}
#////////////{hmo}////////////#
if($data == "dstart" and $hmo['st'] == "❌" and in_array($from_id2,$admin)){
bot('EditMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id2,
'text'=>"• تم مسح رساله start والرجوع الى الرساله الاصلية !",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"HMO"]],
]])
]);
$hmo['st'] = "✅";
$hmo['data'] = "stop";
$hmo['start'] ="
نص الاستارت
";
file_put_contents("data.json",json_encode($hmo));
}
#////////////{hmo}////////////#
if($data == "HMO" and in_array($from_id2,$admin)){
bot('EditMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id2,
"text"=>"• اهلا بك في لوحه الأدمن الخاصه بالبوت 🤖

- يمكنك التحكم في البوت الخاص بك من هنا
~~~~~~~~~~~~~~~~~ ",
 'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>'true',
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[

[['text'=>'• عمل البوت : '.$i4.' •' ,'callback_data'=>"bot"],['text'=>'اشعارات الدخول '.$o1.'' ,'callback_data'=>"o1"]],
[['text'=>'اشعارات الاستخدام '.$o2.'','callback_data'=>"o2"]],
[['text'=>"• الاشتراك •" ,'callback_data'=>"ch"],['text'=>"• رفع ادمن •" ,'callback_data'=>"3"]],
[['text'=>"• اذاعة •" ,'callback_data'=>"1"],['text'=>"• الاحصائيات •" ,'callback_data'=>"2"]],
]])
]);
$hmo['data'] = "stop";
file_put_contents("data.json",json_encode($hmo));
}
#////////////{hmo}////////////#
$hmoinline = $hmo['hmoinline'];
$alch1 = $hmo['ch1'];
$alch2 = $hmo['ch2'];
if($data == "ch" and in_array($from_id2,$admin)){
bot('EditMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id2,
"text"=>"• اهلا عزيزي مطور 
• اليك قائمه الاشتراك اجباري 
- - - - - - - - - - - - 
",
 'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>'true',
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"$alch1" ,'callback_data'=>"alch1"]],
[['text'=>"$alch2" ,'callback_data'=>"alch2"]],
[['text'=>"• اضف قناة اولا •" ,'callback_data'=>"ch1"],['text'=>"• اضف قناة ثانية •" ,'callback_data'=>"ch2"]],
[['text'=>"• ازرار شفافة $hmoinline •" ,'callback_data'=>"hmoinline"]],
[['text'=>"• رجوع •" ,'callback_data'=>"HMO"]],
]])
]);
$hmo['data'] = "stop";
file_put_contents("data.json",json_encode($hmo));
}
#////////////{hmo}////////////#
if($data == "ch1" and in_array($from_id2,$admin)){
bot('EditMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id2,
'text'=>'• الآن قم بارسال معرف قناتك بدون @',
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"HMO"]],
]])
]);
$hmo['c'] = "ch2";
file_put_contents("data.json",json_encode($hmo));
}
if($text and $hmo['c'] == "ch2" and in_array($from_id,$admin)){
$no2 = str_replace('@','',$text);
	$no2 = str_replace('t.me//','',$no2);
	$no2 = str_replace('telegram','',$no2);
	$no2 = str_replace('.me','',$no2);
	$no2 = str_replace('//','',$no2);
	$no2 = str_replace('https://','',$no2);
bot("sendmessage",[
"chat_id"=>$chat_id,
"text"=>"• تم اضافه القناة [@$no2]
• قم برفع البوت ادمن في القناة
",
]);
$hmo['ch1'] = "@$text";
$hmo['data'] = "stop";
$hmo['c'] = "stop";
file_put_contents("data.json",json_encode($hmo));
}
#////////////{hmo}////////////#
if($data == "ch2" and in_array($from_id2,$admin)){
bot('EditMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id2,
'text'=>'• الآن قم بارسال معرف قناتك بدون @',
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"HMO"]],
]])
]);
$hmo['data'] = "ch2";
file_put_contents("data.json",json_encode($hmo));
}
if($text and $hmo['data'] == "ch2" and in_array($from_id,$admin)){
	$no2 = str_replace('@','',$text);
	$no2 = str_replace('t.me//','',$no2);
	$no2 = str_replace('telegram','',$no2);
	$no2 = str_replace('.me','',$no2);
	$no2 = str_replace('//','',$no2);
	$no2 = str_replace('https://','',$no2);
bot("sendmessage",[
"chat_id"=>$chat_id,
"text"=>"• تم اضافه القناة [@$no2]
• قم برفع البوت ادمن في القناة
",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"HMO"]],
]])
]);
$hmo['ch2'] = "@$no2";
$hmo['data'] = "stop";
file_put_contents("data.json",json_encode($hmo));
}
#////////////{hmo}////////////#
if($data == "alch1" and in_array($from_id2,$admin)){
bot('EditMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id2,
'text'=>'• تم حذف القناة '.$hmo['ch1'].' من الإشتراك الإجباري ',
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"HMO"]],
]])
]);
unset($hmo['ch1']);
file_put_contents("data.json",json_encode($hmo));
}
#////////////{hmo}////////////#
if($data == "alch2" and in_array($from_id2,$admin)){
bot('EditMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id2,
'text'=>'• تم حذف القناة '.$hmo['ch2'].' من الإشتراك الإجباري ',
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"HMO"]],
]])
]);
$hmo['data'] = "stop";
unset($hmo['ch2']);
file_put_contents("data.json",json_encode($hmo));
}
#////////////{hmo}////////////#
if($data == "hmoinline" and in_array($from_id2,$admin)){
if($hmo['hmoinline']!="✅"){
$i3 = "✅";
}else{
$i3 = "❌";
}
$hmo['hmoinline'] = $i3;
file_put_contents("data.json",json_encode($hmo));
$hmoinline = $hmo['hmoinline'];
bot('editMessageReplyMarkup',[
'chat_id'=>$update->callback_query->message->chat->id,
'message_id'=>$update->callback_query->message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"$alch1" ,'callback_data'=>"alch1"]],
[['text'=>"$alch2" ,'callback_data'=>"alch2"]],
[['text'=>"• اضف قناة اولا •" ,'callback_data'=>"ch1"],['text'=>"• اضف قناة ثانية •" ,'callback_data'=>"ch2"]],
[['text'=>"• ازرار شفافة $hmoinline •" ,'callback_data'=>"hmoinline2"]],
[['text'=>"• رجوع •" ,'callback_data'=>"HMO"]],
]])
]);
$hmo['data'] = "stop";
$hmo['inlinech1'] = $hmo['ch1'];
$hmo['inlinech2'] = $hmo['ch2'];
file_put_contents("data.json",json_encode($hmo));
}
#////////////{hmo}////////////#
if($data == "hmoinline2" and in_array($from_id2,$admin)){
if($hmo['hmoinline']!="✅"){
$i3 = "✅";
}else{
$i3 = "❌";
}
$hmo['hmoinline'] = $i3;
file_put_contents("data.json",json_encode($hmo));
$hmoinline = $hmo['hmoinline'];
bot('editMessageReplyMarkup',[
'chat_id'=>$update->callback_query->message->chat->id,
'message_id'=>$update->callback_query->message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"$alch1" ,'callback_data'=>"alch1"]],
[['text'=>"$alch2" ,'callback_data'=>"alch2"]],
[['text'=>"• اضف قناة اولا •" ,'callback_data'=>"ch1"],['text'=>"• اضف قناة ثانية •" ,'callback_data'=>"ch2"]],
[['text'=>"• ازرار شفافة $hmoinline •" ,'callback_data'=>"hmoinline"]],
[['text'=>"• رجوع •" ,'callback_data'=>"HMO"]],
]])
]);
$hmo['data'] = "stop";
unset($hmo['inlinech1']);
unset($hmo['inlinech2']);
file_put_contents("data.json",json_encode($hmo));
}
#////////////{hmo}////////////#
if($data == "1" and in_array($from_id2,$admin)){
bot('EditMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id2,
'text'=>'*• مرحبا بك في قسم الاذاعه 🔥*

- عدد الخاص : '.$hmo['id'].'

- عدد المحظورين : '.$hmo['ban']
,
 'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>'true',
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"اذاعه للخاص",'callback_data'=>"msg"],['text'=>"اذاعه توجية",'callback_data'=>"to"]],
[['text'=>"• رجوع •" ,'callback_data'=>"HMO"]],
]])
]);
$hmo['data'] = "stop";
file_put_contents("data.json",json_encode($hmo));
}
#////////////{hmo}////////////#
if($data == "msg" and in_array($from_id2,$admin)){
bot('EditMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id2,
'text'=>"
• ارسال الان الكليشه ( نص او جميع الميديا ) 
• يمكنك استخدام كود جاهز في الاذاعه او يمكنك استخدام الماركداون
",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"• الغاء •" ,'callback_data'=>"HMO"]],
]])
]);
$hmo['data'] = "send";
file_put_contents("data.json",json_encode($hmo));
}
if(!$data and $hmo['data'] == 'send' and in_array($from_id,$admin)){
foreach($hmo['id'] as $all){
if($text)
bot('sendMessage', [
'chat_id'=>$all,
'text'=>"$text",
'parse_mode'=>"MARKDOWN",
'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
]);
if($photo)
bot('sendphoto', [
'chat_id'=>$all,
'photo'=>$photo_id,
'caption'=>$caption,
'parse_mode'=>"MARKDOWN",
'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
]);
if($video)
bot('Sendvideo',[
'chat_id'=>$all,
'video'=>$video_id,
'caption'=>$caption,
'parse_mode'=>"MARKDOWN",
'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
]);
if($video_note)
bot('Sendvideonote',[
'chat_id'=>$all,
'video_note'=>$video_note_id,
]);
if($sticmkar)
bot('Sendsticmkar',[
'chat_id'=>$all,
'sticmkar'=>$sticmkar_id,
'parse_mode'=>"MARKDOWN",
'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
]);
if($file)
bot('SendDocument',[
'chat_id'=>$all,
'document'=>$file_id,
'caption'=>$caption,
'parse_mode'=>"MARKDOWN",
'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
]);
if($music)
bot('Sendaudio',[
'chat_id'=>$all,
'audio'=>$music_id,
'caption'=>$caption,
'parse_mode'=>"MARKDOWN",
'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
]);
if($voice)
bot('Sendvoice',[
'chat_id'=>$all,
'voice'=>$voice_id,
'caption'=>$caption,
'parse_mode'=>"MARKDOWN",
'parse_mode'=>"HTML",
'disable_web_page_preview'=>true,
]);
}
	     for($i=0;$i<count($hmo['id']); $i++){
$ok = bot('sendChatAction' , ['chat_id' =>$hmo['id'][$i],
'action' => 'typing' ,])->ok;
if($hmo['id'][$i] != "" and $ok != 1){
file_put_contents("hmo.txt",$hmo['id'][$i]
,FILE_APPEND);
}}
$ooo = explode("\n",file_get_contents("hmo.txt"));
$iii = count($ooo) - 1;
$mmm = $count - $iii;
					bot('sendmessage',[
	'chat_id'=>$chat_id, 
'text'=>"
• تم الاذاعة بنجاح 🎉

• الاعضاء الذين شاهدو الاذاعه {$mmm} عضو حقيقي
• الاعضاء الذين قامو بحظر البوت {$iii}

• عدد العضاء الكلي : {".$hmo['id']."}
",
'parse_mode'=>"Markdown",
	'reply_to_meesage_id'=>$message_id,
]);
$hmo['data'] = "step";
unlink("hmo.txt");
file_put_contents("data.json",json_encode($hmo));
}
#////////////{hmo}////////////#
if($data == "2" and in_array($from_id2,$admin)){
bot('EditMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id2,
'text'=>'مرحبا بك في قسم الاحصائيات 📊

- عدد المستخدمين في الخاص : '.$hmh['id'].'

- عدد المحظورين : '.$hmo['ban']
,
 'parse_mode'=>"MarkDown",
'disable_web_page_preview'=>'true',
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"• مسح المحضورين •" ,'callback_data'=>"de1"]],
[['text'=>"• حظر شخص •" ,'callback_data'=>"de2"],['text'=>"• الغاء حظر الشخص •" ,'callback_data'=>"de3"]],
[['text'=>"• اذاعة •" ,'callback_data'=>"1"]],
[['text'=>"• رجوع •" ,'callback_data'=>"HMO"]],
]])
]);
$hmo['data'] = "stop";
file_put_contents("data.json",json_encode($hmo));
}
#////////////{hmo}////////////#
if($data == "3" and in_array($from_id2,$admin)){
$mkay=[];
foreach ($hmo['admin'] as $ad){
$mkay[inline_keyboard][]=[[text=>"$ad",callback_data=>"del#$ad"]];
}
$mkay[inline_keyboard][]=[[text=>"اضف ادمن ➕",callback_data=>"add_admin"]];
$mkay[inline_keyboard][]=[[text=>"• رجوع •",callback_data=>"HMO"]];
bot('EditMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id2,
'text'=>"
• مرحبا بك في الادمنيه 👮‍♀️
- يمكنك رفع ادمنيه في البوت او حذفهم 

- يمكن للادمنيه تحكم في لوحه البوت مثلك ولا يمكنهم رفع ادمنيه او استلام رسائل الموجهة .
- - - - - - - - - - - - 
",
reply_markup=>json_encode($mkay)
]);
}
$ex = explode("#", $data);
if($ex[0] == "del"){
$ser = array_search($ex[1],$hmo["admin"]);
unset($hmo["admin"][$ser]);
file_put_contents("data.json",json_encode($hmo));
$mkay=[];
foreach ($hmo['admin'] as $ad){
$mkay[inline_keyboard][]=[[text=>"$ad",callback_data=>"del#$ad"]];
}
$mkay[inline_keyboard][]=[[text=>"اضف ادمن ➕",callback_data=>"add_admin"]];
$mkay[inline_keyboard][]=[[text=>"• رجوع •",callback_data=>"HMO"]];
bot('editMessageReplyMarkup',[
'chat_id'=>$update->callback_query->message->chat->id,
'message_id'=>$update->callback_query->message->message_id,
reply_markup=>json_encode($mkay)
]);
}
#////////////{hmo}////////////#
if($data == "add_admin" and $from_id2 == $a1 ){
bot('EditMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id2,
'text'=>"الان ارسل ايدي الشخص •",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"• الغاء •" ,'callback_data'=>"HMO"]],
]])
]);
$hmo['data'] = "go";
file_put_contents("data.json",json_encode($hmo));
}
if($text  and $from_id == $a1 and $hmo['data'] == "go" and !in_array($text,$hmo['id'])){
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"$text ليس عضو بالبوت •",
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"HMO"]],
]])
]);
}
$test = $hmo['admin'];
if($text and $from_id == $a1 and $hmo['data'] == "go" and in_array($text,$test)){
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"العضو مرفوع ادمن •",
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"• رجوع •" ,'callback_data'=>"HMO"]],
]])
]);
$hmo['data'] = "stop";
file_put_contents("data.json",json_encode($hmo));
exit();
}
if($text and $from_id == $a1 and $hmo['data'] == "go" and in_array($text,$hmo['id'])){
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"
تم اضافه $text ادمن ✅
",
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"HMO"]],
]])
]);
$hmo['admin'][] = $text;
$hmo['data'] = "stop";
file_put_contents("data.json",json_encode($hmo));
}
if($data == "to" and in_array($from_id2,$admin)){
bot('EditMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id2,
'text'=>"• ارسال الان الكليشه !",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"رجوع",'callback_data'=>"HMO"]],
]])
]);
$hmo['data'] = "to";
file_put_contents("data.json",json_encode($hmo));
}
if($message and $hmo['data'] == "to" and in_array($from_id,$admin)){
bot("sendmessage",[
"chat_id"=>$chat_id,
"text"=>'جاري التوجية',
 'reply_markup'=>json_encode([ 
  'inline_keyboard'=>[
[['text'=>"رجوع",'callback_data'=>"HMO"]],
]])
]);
for($i=0;$i<count($hmo['id']); $i++){
bot('forwardMessage', [
'chat_id'=>$hmo['id'][$i],
'from_chat_id'=>$from_id,
'message_id'=>$message->message_id
]);
$hmo['data'] = "stop";
file_put_contents("data.json",json_encode($hmo));
}
$ok = bot('sendChatAction' , ['chat_id' =>$hmo['id'][$i],
'action' => 'typing' ,])->ok;
if($hmo['id'][$i] != "" and $ok != 1){
file_put_contents("A5.txt",$hmo['id'][$i]
,FILE_APPEND);
}
$ooo = $hmo['id'];
$iii = count($ooo) - 1;
$mmm = $count - $iii;
					bot('sendmessage',[
	'chat_id'=>$chat_id, 
'text'=>"
• تم الاذاعة بنجاح 🎉

• الاعضاء الذين شاهدو الاذاعه {$mmm} عضو حقيقي
• الاعضاء الذين قامو بحظر البوت {$iii}

• عدد العضاء الكلي : {".$hmo['id']."}
",
'parse_mode'=>"Markdown",
	'reply_to_meesage_id'=>$message_id,
]);
$hmo['data'] = "stop";
unlink("hmo.txt");
file_put_contents("data.json",json_encode($hmo));
}
if($data == "o1" and in_array($from_id2,$admin)){
if($hmo['o1']!="✅"){
$i1 = "✅";
}else{
$i1 ="❌";
}
$hmo['o1'] = $i1;
file_put_contents("data.json",json_encode($hmo));
$o1 = $hmo['o1'];
bot('editMessageReplyMarkup',[
'chat_id'=>$update->callback_query->message->chat->id,
'message_id'=>$update->callback_query->message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• عمل البوت : '.$i4.' •' ,'callback_data'=>"bot"],
['text'=>'اشعارات الدخول '.$o1.'' ,'callback_data'=>"o1"]],
[['text'=>'اشعارات الاستخدام '.$o2.'' ,'callback_data'=>"o2"]],
[['text'=>"• الاشتراك •" ,'callback_data'=>"ch"]],
[['text'=>"• اذاعة •" ,'callback_data'=>"1"],['text'=>"• الاحصائيات •" ,'callback_data'=>"2"]],
]])
]);
$hmo['data'] = "stop";
file_put_contents("data.json",json_encode($hmo));
}
#////////////{hmo}////////////#
if($user != null){
$med = "@$user";
}elseif($user == null){
$med = "لا يملك معرف";
}
if($text == "/start" and $from_id != $admin and $o1 == "✅" and !in_array($from_id,$hmo['id'])){
bot('sendmessage',[
'chat_id'=>$a1,
'text'=>'
٭ تم دخول شخص جديد الى البوت الخاص بك 👾
    -----------------------
• معلومات العضو الجديد .

• الاسم : '.$name.'
• المعرف : '.$med.'
• الايدي : '.$from_id.'
    -----------------------
• عدد الاعضاء الكلي : '.$hmo['id'].'
',
'parse_mode'=>"Markdown",
]);
}
#////////////{hmo}////////////#
if($data == "o2" and in_array($from_id2,$admin)){
if($hmo['o2']!="✅"){
$i2 = "✅";
}else{
$i2 ="❌";
}
$hmo['o2'] = $i2;
file_put_contents("data.json",json_encode($hmo));
$o2 = $hmo['o2'];
bot('editMessageReplyMarkup',[
'chat_id'=>$update->callback_query->message->chat->id,
'message_id'=>$update->callback_query->message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[

[['text'=>'• عمل البوت : '.$i4.' •' ,'callback_data'=>"bot"],['text'=>'اشعارات الدخول '.$o1.'' ,'callback_data'=>"o1"]],
[['text'=>'اشعارات الاستخدام '.$o2.'','callback_data'=>"o2"]],
[['text'=>"• الاشتراك •" ,'callback_data'=>"ch"],['text'=>"• رفع ادمن •" ,'callback_data'=>"3"]],
[['text'=>"• اذاعة •" ,'callback_data'=>"1"],['text'=>"• الاحصائيات •" ,'callback_data'=>"2"]],

]])
]);
$hmo['data'] = "stop";
file_put_contents("data.json",json_encode($hmo));
}

if($message and $text != "/start" and $from_id != $a1 and $o2 == "✅" and !$data){
bot('forwardMessage',[
'chat_id'=>$a1,
'from_chat_id'=>$chat_id,
 'message_id'=>$update->message->message_id,
'text'=>$text,
]);
}
#////////////{hmo}////////////#
if($data == "bot" and in_array($from_id2,$admin)){
if($hmo['bot']!="✅" ){
$i4 = "✅";
}else{
$i4 = "❌";
}

$hmo['bot'] = $i4;
file_put_contents("data.json",json_encode($hmo));
$i4 = $hmo['bot'];
bot('editMessageReplyMarkup',[
'chat_id'=>$update->callback_query->message->chat->id,
'message_id'=>$update->callback_query->message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[

[['text'=>'• عمل البوت : '.$i4.' •' ,'callback_data'=>"bot"],['text'=>'اشعارات الدخول '.$o1.'' ,'callback_data'=>"o1"]],
[['text'=>'اشعارات الاستخدام '.$o2.'','callback_data'=>"o2"]],
[['text'=>"• الاشتراك •" ,'callback_data'=>"ch"],['text'=>"• رفع ادمن •" ,'callback_data'=>"3"]],
[['text'=>"• اذاعة •" ,'callback_data'=>"1"],['text'=>"• الاحصائيات •" ,'callback_data'=>"2"]],

]])
]);
$hmo['data'] = "stop";
file_put_contents("data.json",json_encode($hmo));
}
if($data == "bot" and $hmo['bot'] == "❌" and in_array($from_id2,$admin)){
bot("EditMessageText",[
'chat_id'=>$chat_id2,
'message_id'=>$message_id2,
"text"=>"ارسل كليشه تعطيل البوت",
]);
$hmo['data'] = "bo22";
file_put_contents("data.json",json_encode($hmo));
} 
if($text and $hmo['data'] == "bo22" and in_array($from_id,$admin)){
bot("sendmessage",[
"chat_id"=>$chat_id,
"text"=>"• تم حفظ رساله",
 'reply_markup'=>json_encode([ 
      'inline_keyboard'=>[
[['text'=>'رجوع' ,'callback_data'=>"HMO"]],
]])
]);
$hmo['botst'] = "$text";
$hmo['data'] = "stop";
file_put_contents("data.json",json_encode($hmo));
}
#////////////{hmo}////////////#
if($data =="de1" and $hmo['ban'] == null){
bot('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'message_id'=>$message_id,
'text'=>"لا يوجد محضورين ⚠️",
'show_alert'=>true
]);
}
if($data =="de1" and in_array($from_id,$admin)){
bot('answerCallbackQuery',[
'callback_query_id'=>$update->callback_query->id,
'message_id'=>$message_id,
'text'=>"تم مسح المحضورين ⚠️",
'show_alert'=>true
]);
$hmo['ban'] = null;
file_put_contents("data.json",json_encode($hmo));
}
#////////////{hmo}////////////#
if($data == "de2" and in_array($from_id2,$admin)){
bot('EditMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id2,
'text'=>'• ارسل ايدي شخص للحظر',
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"HMO"]],
]])
]);
$hmo['data'] = "de2";
file_put_contents("data.json",json_encode($hmo));
}
if($text and $hmo['data'] == "de2" and in_array($from_id,$admin)){
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"*تم حظر الشخص من البوت ⛔️*",
'parse_mode'=>"Markdown",
'reply_to_message_id'=>$message->message_id,
]);
bot("sendmessage",[
'chat_id'=>$text,
"text"=>"*تم حظرك من البوت ⛔️*",
]);
$hmo['ban'][] = "$text";
$hmo['data'] = "stop";
file_put_contents("data.json",json_encode($hmo));
}
if($data == "de3" and in_array($from_id2,$admin)){
bot('EditMessageText',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id2,
'text'=>'• ارسل ايدي شخص لالغاء حظر',
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"HMO"]],
]])
]);
$hmo['data'] = "de3";
file_put_contents("data.json",json_encode($hmo));
}
if($text and $hmo['data'] == "de3" and in_array($from_id,$admin)){
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"تم الغاء حظر الشخص من البوت ✅",
'parse_mode'=>"Markdown",
'reply_to_message_id'=>$message->message_id,
]);
bot("sendmessage",[
'chat_id'=>$text,
"text"=>"*تم الغاء حظرك من البوت ✅*",
]);
$mkay = array_search($text,$hmo["ban"]);
unset($hmo["ban"][$mkay]);
$hmo["ban"] = array_values($hmo["ban"]); 
$hmo = json_encode($hmo,true);
$hmo['data'] = "stop";
file_put_contents("data.json",$hmo);
} 
if($message and $hmo['bot'] =="❌"  and !in_array($from_id,$hmo['ban']) and !in_array($from_id,$admin)){
 bot("sendmessage",[
 "chat_id"=>$chat_id,
 "text"=>$hmo['botst']
 ]);
 return false;
}
if($message and in_array($from_id,$hmo['ban'])){
 bot("sendmessage",[
 "chat_id"=>$chat_id,
 "text"=>""
 ]);
 return false;
}
//////////////(hmo)/////////#

if($text == "⌯ تعيين اسم البوت ." and in_array($from_id,$admin)){
file_put_contents("setname.txt","nam");
bot("sendMessage",[
"chat_id"=>$chat_id,
"text"=>"⌯🔮◉← قم بأرسال اسم البوت الان",
'parse_mode'=>"MARKDOWN",
'reply_to_message_id'=>$message_id,
]);
}
if($text && $setnamebot =="nam" and in_array($from_id,$admin)){
file_put_contents("namebot.txt",$text); 
file_put_contents("setname.txt","");
bot("sendmessage",[
"chat_id"=>$chat_id,
"text" =>"
⌯🔮◉← تم تعيين اسم البوت بنجاح
⌯🔮◉←اسمي الان ↫ $text
",
'parse_mode'=>"MARKDOWN",
'reply_to_message_id'=>$message_id,
]);
}

if($text == "/start"){
bot('sendphoto',[
'chat_id'=>$chat_id,
'photo'=>"https://2.top4top.net/p_1280fxflb1.jpg",
'caption'=>"
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
🎤╖ أهلآ بك عزيزي أنا بوت $namebot
⚙️╢ وظيفتي حماية القنوات
✅╢ أضِف البوت إلى قناتك
🔘╢ ارفعهُ » مشرف
⚡️╢ ثم ارسل » تفعيل
⬆️╜ البوت لا يعمل بدون صلاحيه اضافه مشرفين
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
",
'parse_mode'=>"markdown",'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message_id,
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>'- الاوامر .' ,'callback_data'=>"cmd"],['text'=>'- حول .' ,'callback_data'=>"info"]],
[['text'=>"- قناة السورس .",'url'=>"t.me/AlmortagelTech"],['text'=>"- المطور .",'url'=>"t.me/$usermn"]],
[['text'=>"- اضف البوت لقناتك .",'url'=>"https://t.me/$userbot?startchannel"]],
]])
]);
}
if($text == "/start" and in_array($from_id,$admin)){
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"- قم بوضع اسم .",
'disable_web_page_preview'=>'true',
'parse_mode'=>"MarkDown",
'reply_to_message_id'=>$message_id,
'reply_markup'=>json_encode([
"resize_keyboard"=>true,
'keyboard'=>[
[['text'=>'⌯ تعيين اسم البوت .']],
]])
]);
}
if($data == "back" ){
bot('EditMessageCaption',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id2,
'photo' =>"https://2.top4top.net/p_1280fxflb1.jpg",
'caption'=>"
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
🎤╖ أهلآ بك عزيزي أنا بوت $namebot
⚙️╢ وظيفتي حماية القنوات
✅╢ أضِف البوت إلى قناتك
🔘╢ ارفعهُ » مشرف
⚡️╢ ثم ارسل » تفعيل
⬆️╜ البوت لا يعمل بدون صلاحيه اضافه مشرفين
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
",
'parse_mode'=>"markdown",'disable_web_page_preview'=>true,
"reply_markup"=>json_encode([
"inline_keyboard"=>[
[['text'=>'- الاوامر .' ,'callback_data'=>"cmd"],['text'=>'- حول .' ,'callback_data'=>"info"]],
[['text'=>"- قناة السورس .",'url'=>"t.me/AlmortagelTech"],['text'=>"- المطور .",'url'=>"t.me/$usermn"]],
[['text'=>"- اضف البوت لقناتك .",'url'=>"https://t.me/$userbot?startchannel"]],
]])]);}
if($data == "info" ){
bot('EditMessageCaption',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id2,
'photo' =>"https://2.top4top.net/p_1280fxflb1.jpg",
'caption'=>'
╭──── • ◈ • ────╮
么 [𝗦𝗢𝗨𝗥𝗖𝗘](https://t.me/AlmortagelTech)
么 [𝗔𝗟𝗠𝗢𝗥𝗧𝗔𝗚𝗘𝗟](https://t.me/Almortagel_12)
╰──── • ◈ • ────╯
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼
',
'parse_mode'=>"markdown",'disable_web_page_preview'=>true,
"reply_markup"=>json_encode([
"inline_keyboard"=>[
[['text'=>"- رجوع .",'callback_data'=>"back"]],
]])]);}
if($data == "cmd" ){
bot('EditMessageCaption',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id2,
'photo' =>"https://2.top4top.net/p_1280fxflb1.jpg",
'caption'=>'
⚙️╖⁩ ❬ م1 ❭ اوامر حماية القناه ⇊
💫╜ ❬ م2 ❭ اوامر الحمايه من التفليش ⇊
',
'parse_mode'=>"markdown",'disable_web_page_preview'=>true,
"reply_markup"=>json_encode([
"inline_keyboard"=>[
[['text'=>"⨳ م1",'callback_data'=>"m1"],['text'=>"⨳ م2",'callback_data'=>"m2"]],
[['text'=>"- رجوع .",'callback_data'=>"back"]],
[['text'=>"- اضف البوت لقناتك .",'url'=>"https://t.me/$userbot?startchannel"]],
]])]);}
if($data == "m1" ){
bot('EditMessageCaption',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id2,
'photo' =>"https://2.top4top.net/p_1280fxflb1.jpg",
'caption'=>'
⚙️⁩ ❬ م1 ❭ اوامر حماية القناه ⇊
════════ ××× ════════ٴ
🔐 ╢ قفل «» فتح + الامر 
════════ ××× ════════ٴ
📮╖ المتحركه
📜╢ الملصقات
📸╢ الصور
📽️╢ الفيديوهات
🎟╢ التوجيه
📂╢ المواقع
🎥╢ الصوت
⏏️╢ الروابط
🔊╜ المعرفات
════════ ××× ════════ٴ
',
'parse_mode'=>"markdown",'disable_web_page_preview'=>true,
"reply_markup"=>json_encode([
"inline_keyboard"=>[
[['text'=>"- رجوع .",'callback_data'=>"cmd"]],
[['text'=>"- اضف البوت لقناتك .",'url'=>"https://t.me/$userbot?startchannel"]],
]])]);}
if($data == "m2" ){
bot('EditMessageCaption',[
'chat_id'=>$chat_id2,
'message_id'=>$message_id2,
'photo' =>"https://2.top4top.net/p_1280fxflb1.jpg",
'caption'=>'
⚙️⁩ ❬ م2 ❭ اوامر حماية القناه من التفليش ⇊
════════ ××× ════════ٴ
🔐 ╖ ارسل /admin ثم ايدي العضو
🧾 ╢ مثال /admin 27274549
⏏️ ╜ تنزيل الادمنيه
',
'parse_mode'=>"markdown",'disable_web_page_preview'=>true,
"reply_markup"=>json_encode([
"inline_keyboard"=>[
[['text'=>"- رجوع .",'callback_data'=>"cmd"]],
[['text'=>"- اضف البوت لقناتك .",'url'=>"https://t.me/$userbot?startchannel"]],
]])]);}

if($ccc and $tt){
bot('sendmessage',[
'chat_id'=>$ccc,
'text'=>"- ارفع البوت بصلاحيه اضافه مشرفين ثم اضفني مره اخره ."]); 
bot('leaveChat',[
'chat_id'=>$ccc
]);
}
if($ccc and $ba){
} else{ 
if($ccc){
bot('sendmessage',[
'chat_id'=>$ccc,
'text'=>"- ارفع البوت بصلاحيه اضافه مشرفين ثم اضفني مره اخره ."]); 
bot('leaveChat',[
'chat_id'=>$ccc
]);
}} 
if($ban=="kicked"){
bot('sendmessage',[
'chat_id'=>$chatban, 
'text'=>"
تم حظر عضو بواسطه @$user_admen 
اسم المشرف $name_admen 
ايدي المشرف $id_admen 
العضو المحظور 😔 
يوزر @$ban_user 
الاسم $ban_name 
الايدي $ban_id
تم حذف @$user_admen من الادمنيه
"
]);
bot('promoteChatMember',[
'user_id'=>$id_admen,
'chat_id'=>$chatban, 
"can_change_info"=>false, 
"can_post_messages"=>false, 
"can_edit_messages"=>false, 
"can_delete_messages"=>false, 
"can_invite_users"=>false, 
"can_restrict_members"=>false, 
"can_pin_messages"=>false, 
"can_manage_video_chats"=>false, 
"can_promote_members"=>false
]); 
bot('sendmessage',[
'chat_id'=>$chatban, 
'text'=>"
- عزيزي المالك .
- لقد قام احد الادمنيه بطرد عضو .
- وقمت بتنزيله من الادمنيه للأمان .
"
]);
}
$admen = str_replace("/admin ","",$text1);
if($text1 == "/admin $admen"){
bot('promoteChatMember',[
'user_id'=>"$admen", 
'chat_id'=>$chat, 
"can_change_info"=>false, 
"can_post_messages"=>true, 
"can_edit_messages"=>false, 
"can_delete_messages"=>false, 
"can_invite_users"=>true, 
"can_restrict_members"=>false, 
"can_pin_messages"=>true, 
"can_manage_video_chats"=>true, 
"can_promote_members"=>false
]); 
bot('sendmessage',[
'chat_id'=>$chat,
'text'=>"- تم رفعه ادمن ."
]); 
}
if($text1 == "تنزيل الكل"){
$up = json_decode(file_get_contents("https://api.telegram.org/bot$token/getChatAdministrators?chat_id=$chat"),true);
$result = $up["result"];
foreach($result as $key=>$value){
$found = $result[$key]["status"];
if($found == "creator"){
$owner = $result[$key]["user"]["id"];
$owner2 = $result[$key]["user"]["id"];
}
if($found == "administrator"){
if($result[$key]["user"]["first_name"] == true){
$innames = str_replace(['[',']'],'',$result[$key]["user"]["id"]);
$msg = $msg.""."virus"."$innames";
}
}
}
$virus = explode("virus","$msg");
foreach($virus as $i){
bot('promoteChatMember',[
'user_id'=>$i, 
'chat_id'=>$chat, 
"can_change_info"=>false, 
"can_post_messages"=>false, 
"can_edit_messages"=>false, 
"can_delete_messages"=>false, 
"can_invite_users"=>false, 
"can_restrict_members"=>false, 
"can_pin_messages"=>false, 
"can_promote_members"=>false
]); 
}
bot('sendmessage',[
'chat_id'=>$chat,
'text'=>"- تم تنزيل جميع الادمنيه المرفوعين عبر البوت ."
]); 
}
#تم ازاله الميزه لعيون طه وللأمان والثقه
$json_security_channels = json_decode(file_get_contents("data/$chid.json"),true);
if($json_security_channels["lock"]["document"] == "close"){
if(isset($document )){
bot('deletemessage',[
'chat_id'=>$chid,
'message_id'=>$messageid
]);
}
}
if($json_security_channels["lock"]["sticker"] == "close"){
if(isset($sticker )){
bot('deletemessage',[
'chat_id'=>$chid,
'message_id'=>$messageid
]);
}
}
if($json_security_channels["lock"]["photo"] == "close"){
if(isset($photo )){
bot('deletemessage',[
'chat_id'=>$chid,
'message_id'=>$messageid
]);
}
}
if($json_security_channels["lock"]["video"] == "close"){
if(isset($video )){
bot('deletemessage',[
'chat_id'=>$chid,
'message_id'=>$messageid
]);
}
}
if($json_security_channels["lock"]["forward"] == "close"){
if(isset($forward )){
bot('deletemessage',[
'chat_id'=>$chid,
'message_id'=>$messageid
]);
}
}
if($json_security_channels["lock"]["contact"] == "close"){
if(isset($contact )){
bot('deletemessage',[
'chat_id'=>$chid,
'message_id'=>$messageid
]);
}
}
if($json_security_channels["lock"]["audio"] == "close"){
if(isset($audio )){
bot('deletemessage',[
'chat_id'=>$chid,
'message_id'=>$messageid
]);
}
}
if($json_security_channels["lock"]["link"] == "close"){
if(preg_match('/^(.*)([Hh]ttp|[Hh]ttps|t.me)(.*)|([Hh]ttp|[Hh]ttps|t.me)(.*)|(.*)([Hh]ttp|[Hh]ttps|t.me)|(.*)[Tt]elegram.me(.*)|[Tt]elegram.me(.*)|(.*)[Tt]elegram.me|(.*)[Tt].me(.*)|[Tt].me(.*)|(.*)[Tt].me|(.*)telesco.me|telesco.me(.*)/i',$update->channel_post->text)){
bot('deleteMessage',[
'chat_id'=>$chid,
'message_id'=>$messageid
]);
}
}
if($json_security_channels["lock"]["username"] == "close"){
if (strstr($text ,"@") == true or strstr($caption,"@") == true) {
bot('deletemessage',[
'chat_id'=>$chid,
'message_id'=>$messageid
]);
}
}
if($chtext == "تفعيل" ){
$json_security_channels = '{"lock": {"document": "open" "username": "open" "photo": "open" "link": "open" "video": "open" "forward": "open" "contact": "open" "audio": "open" "sticker": "open"},}';
$json_security_channels = json_decode($json_security_channels,true);
$json_security_channels = json_encode($json_security_channels,true);
file_put_contents("data/$chid.json",$json_security_channels);
bot('sendmessage',[
'chat_id'=>$chid,
'text'=>"
☑️ ¦ تم تفعيل البوت في القناة
📡 ¦ ايدي القناة `$chid`
",'parse_mode'=>"markdown",
'reply_to_message_id'=>$messageid,
]);
}
if($chtext =="قفل الصور" ){
$json_security_channels["lock"]["photo"]="close";
$json_security_channels = json_encode($json_security_channels,true);
file_put_contents("data/$chid.json",$json_security_channels);
bot('sendmessage',[
'chat_id'=>$chid,
'text'=>"🔐 ¦ تم قفل $photos بنجاح √",
'reply_to_message_id'=>$messageid,
]);
}
if($chtext =="فتح الصور" ){
$json_security_channels["lock"]["photo"]="open";
$json_security_channels = json_encode($json_security_channels,true);
file_put_contents("data/$chid.json",$json_security_channels);
bot('sendmessage',[
'chat_id'=>$chid,
'text'=>"🔓 ¦ تم فتح $photos بنجاح √",
'reply_to_message_id'=>$messageid,
]);
}
if($chtext =="قفل الفيديو" ){
$json_security_channels["lock"]["video"]="close";
$json_security_channels = json_encode($json_security_channels,true);
file_put_contents("data/$chid.json",$json_security_channels);
bot('sendmessage',[
'chat_id'=>$chid,
'text'=>"🔐 ¦ تم قفل $videos بنجاح √",
'reply_to_message_id'=>$messageid,
]);
}
if($chtext =="فتح الفيديو" ){
$json_security_channels["lock"]["video"]="open";
$json_security_channels = json_encode($json_security_channels,true);
file_put_contents("data/$chid.json",$json_security_channels);
bot('sendmessage',[
'chat_id'=>$chid,
'text'=>"🔓 ¦ تم فتح $videos بنجاح √",
'reply_to_message_id'=>$messageid,
]);
}
if($chtext =="قفل الملصقات" ){
$json_security_channels["lock"]["sticker"]="close";
$json_security_channels = json_encode($json_security_channels,true);
file_put_contents("data/$chid.json",$json_security_channels);
bot('sendmessage',[
'chat_id'=>$chid,
'text'=>"🔐 ¦ تم قفل $stickers بنجاح √",
'reply_to_message_id'=>$messageid,
]);
}
if($chtext =="فتح الملصقات" ){
$json_security_channels["lock"]["sticker"]="open";
$json_security_channels = json_encode($json_security_channels,true);
file_put_contents("data/$chid.json",$json_security_channels);
bot('sendmessage',[
'chat_id'=>$chid,
'text'=>"🔓 ¦ تم فتح $stickers بنجاح √",
'reply_to_message_id'=>$messageid,
]);
}
if($chtext =="قفل المتحركة" ){
$json_security_channels["lock"]["document"]="close";
$json_security_channels = json_encode($json_security_channels,true);
file_put_contents("data/$chid.json",$json_security_channels);
bot('sendmessage',[
'chat_id'=>$chid,
'text'=>"🔐 ¦ تم قفل $documents بنجاح √",
'reply_to_message_id'=>$messageid,
]);
}
if($chtext =="فتح المتحركة" ){
$json_security_channels["lock"]["document"]="open";
$json_security_channels = json_encode($json_security_channels,true);
file_put_contents("data/$chid.json",$json_security_channels);
bot('sendmessage',[
'chat_id'=>$chid,
'text'=>"🔓 ¦ تم فتح $documents بنجاح √",
'reply_to_message_id'=>$messageid,
]);
}
if($chtext =="قفل التوجيه" ){
$json_security_channels["lock"]["forward"]="close";
$json_security_channels = json_encode($json_security_channels,true);
file_put_contents("data/$chid.json",$json_security_channels);
bot('sendmessage',[
'chat_id'=>$chid,
'text'=>"🔐 ¦ تم قفل $forwards بنجاح √",
'reply_to_message_id'=>$messageid,
]);
}
if($chtext =="فتح التوجيه" ){
$json_security_channels["lock"]["forward"]="open";
$json_security_channels = json_encode($json_security_channels,true);
file_put_contents("data/$chid.json",$json_security_channels);
bot('sendmessage',[
'chat_id'=>$chid,
'text'=>"🔓 ¦ تم فتح $forwards بنجاح √",
'reply_to_message_id'=>$messageid,
]);
}
if($chtext =="قفل الصوت" ){
$json_security_channels["lock"]["audio"]="close";
$json_security_channels = json_encode($json_security_channels,true);
file_put_contents("data/$chid.json",$json_security_channels);
bot('sendmessage',[
'chat_id'=>$chid,
'text'=>"🔐 ¦ تم قفل $audios بنجاح √",
'reply_to_message_id'=>$messageid,
]);
}
if($chtext =="فتح الصوت" ){
$json_security_channels["lock"]["audio"]="open";
$json_security_channels = json_encode($json_security_channels,true);
file_put_contents("data/$chid.json",$json_security_channels);
bot('sendmessage',[
'chat_id'=>$chid,
'text'=>"🔓 ¦ تم فتح $audios بنجاح √",
'reply_to_message_id'=>$messageid,
]);
}
if($chtext =="قفل الموقع" ){
$json_security_channels["lock"]["contact"]="close";
$json_security_channels = json_encode($json_security_channels,true);
file_put_contents("data/$chid.json",$json_security_channels);
bot('sendmessage',[
'chat_id'=>$chid,
'text'=>"🔐 ¦ تم قفل $contacts بنجاح √",
'reply_to_message_id'=>$messageid,
]);
}
if($chtext =="فتح الموقع" ){
$json_security_channels["lock"]["contact"]="open";
$json_security_channels = json_encode($json_security_channels,true);
file_put_contents("data/$chid.json",$json_security_channels);
bot('sendmessage',[
'chat_id'=>$chid,
'text'=>"🔓 ¦ تم فتح $contacts بنجاح √",
'reply_to_message_id'=>$messageid,
]);
}
if($chtext =="قفل الروابط" ){
$json_security_channels["lock"]["link"]="close";
$json_security_channels = json_encode($json_security_channels,true);
file_put_contents("data/$chid.json",$json_security_channels);
bot('sendmessage',[
'chat_id'=>$chid,
'text'=>"🔐 ¦ تم قفل $links بنجاح √",
'reply_to_message_id'=>$messageid,
]);
}
if($chtext =="فتح الروابط" ){
$json_security_channels["lock"]["link"]="open";
$json_security_channels = json_encode($json_security_channels,true);
file_put_contents("data/$chid.json",$json_security_channels);
bot('sendmessage',[
'chat_id'=>$chid,
'text'=>"🔓 ¦ تم فتح $links بنجاح √",
'reply_to_message_id'=>$messageid,
]);
}
if($chtext =="قفل المعرفات" ){
$json_security_channels["lock"]["username"]="close";
$json_security_channels = json_encode($json_security_channels,true);
file_put_contents("data/$chid.json",$json_security_channels);
bot('sendmessage',[
'chat_id'=>$chid,
'text'=>"🔐 ¦ تم قفل $usernames بنجاح √",
'reply_to_message_id'=>$messageid,
]);
}
if($chtext =="فتح المعرفات" ){
$json_security_channels["lock"]["username"]="open";
$json_security_channels = json_encode($json_security_channels,true);
file_put_contents("data/$chid.json",$json_security_channels);
bot('sendmessage',[
'chat_id'=>$chid,
'text'=>"🔓 ¦ تم فتح $usernames بنجاح √",
'reply_to_message_id'=>$messageid,
]);
}
  
 if($text == "دي"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"يمشوك بيهة هاي مطي",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "ههه" ){
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>"دوِمٰ̲ہ ضۜہٰٰحہٰٰڪٰྀہٰٰٖتَہَٰڪٰྀہٰٰٖ 🙊😻" ,
'reply_to_message_id'=>$message->message_id,
]);
}
if($text == "🚶🏿‍♂💔"){
bot( sendsticker,[
 chat_id =>$chat_id, 
 sticker =>"https://t.me/eee_o/54",
 reply_to_message_id =>$message->message_id, 
]);
}
if($text == "🤤"){
bot( sendsticker,[
 chat_id =>$chat_id, 
 sticker =>"https://t.me/eee_o/55",
 reply_to_message_id =>$message->message_id, 
]);
}
if($text == "🤓"){
bot( sendsticker,[
 chat_id =>$chat_id, 
 sticker =>"https://t.me/eee_o/56",
 reply_to_message_id =>$message->message_id, 
]);
}
if($text == "🙃"){
bot( sendsticker,[
 chat_id =>$chat_id, 
 sticker =>"https://t.me/eee_o/57",
 reply_to_message_id =>$message->message_id, 
]);
}
if($text == "😻"){
bot( sendsticker,[
 chat_id =>$chat_id, 
 sticker =>"https://t.me/eee_o/58",
 reply_to_message_id =>$message->message_id, 
]);
}
if($text == "🙆‍♀"){
bot( sendsticker,[
 chat_id =>$chat_id, 
 sticker =>"https://t.me/eee_o/59",
 reply_to_message_id =>$message->message_id, 
]);
}
if($text == "🌞"){
bot( sendsticker,[
 chat_id =>$chat_id, 
 sticker =>"https://t.me/eee_o/60",
 reply_to_message_id =>$message->message_id, 
]);
}
if($text == "🤦🏿‍♂💔"){
bot( sendsticker,[
 chat_id =>$chat_id, 
 sticker =>"https://t.me/eee_o/61",
 reply_to_message_id =>$message->message_id, 
]);
}
if($text == "🤔"){
bot( sendsticker,[
 chat_id =>$chat_id, 
 sticker =>"https://t.me/eee_o/62",
 reply_to_message_id =>$message->message_id, 
]);
}
if($text == "🙁"){
bot( sendsticker,[
 chat_id =>$chat_id, 
 sticker =>"https://t.me/eee_o/63",
 reply_to_message_id =>$message->message_id, 
]);
}
if($text == "🚶🐕"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"دربالك ليعضك ",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "هه" ){
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>" ھہآيِٰہ ھہمٰ̲ہ تَہَٰسٰٰٓمٰ̲ہئ ضۜہٰٰحہٰٰڪٰྀہٰٰٖھہ☹️ " ,
'reply_to_message_id'=>$message->message_id,
]);
}
if($text == "جوعان" ){
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>" شِٰہٰٰبّہيِٰہڪٰྀہٰٰٖ شِٰہٰٰڪٰྀہٰٰٖد تَہَٰآڪٰྀہٰٰٖوِل وِمٰ̲ہآتَہَٰشِٰہٰٰبّہ؏ۤـہٰٰ😒 " ,
'reply_to_message_id'=>$message->message_id,
]);
}
if($text == "اك" ){
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>"شتحس 🌚💛 " ,
'reply_to_message_id'=>$message->message_id,
]);
}
if($text == "جكجاو" ){
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>" خٰ̐ہليِٰہنَِٰہٰة نَِٰہٰآخٰ̐ہوِذِ رآحہٰٰتَہَٰنَِٰہٰآ 😹🙊 " ,
'reply_to_message_id'=>$message->message_id,
]);
}
if($text == "جاوو" ){
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>" تَہََٰ؏ۤـہٰٰآّإآّإلّ آڪٰྀہٰٰٖلڪٰྀہٰٰٖ شِٰہٰٰيِٰہ قྀ̲ہٰٰٰبّہل لٱ تَہَٰروِحہٰٰ 🌝💛ِٰٰٰٰྀ " ,
'reply_to_message_id'=>$message->message_id,
]);
}
if($text == "كولي" ){
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>"آنَِٰہٰيِٰہ ضۜہٰٰآيِٰہجْۧھہ آبّہقྀ̲ہٰٰٰى ھہنَِٰہٰآ ☹️🚶‍♀ " ,
'reply_to_message_id'=>$message->message_id,
]);
}

if($text == "🙂" ){
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>" ؏ۤـہٰٰوِد صۛہٰٰآيِٰہر ثہٰٰڪٰྀہٰٰٖيِٰہل 😕 " ,
'reply_to_message_id'=>$message->message_id,
]);
}
if($text == "هاي" ){
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>" ھہـآيِٰہآتَہَٰ يِٰہروِحہٰٰيِٰہ 😻👅" ,
'reply_to_message_id'=>$message->message_id,
]);
}
if($text == "😕" ){
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>"ليِٰہشِٰہٰٰ ڪٰྀہٰٰٖآلبّہڪٰྀہٰٰٖ شِٰہٰٰڪٰྀہٰٰٖلڪٰྀہٰٰٖ مٰ̲ہوِ ؏ۤـہٰٰليِٰہنَِٰہٰھہ 🌝🎋 " ,
'reply_to_message_id'=>$message->message_id,
]);
}
if($text == "جوعانة" ){
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>" ٰٰ😒 تَہََٰ؏ۤـہٰٰآّإآّإلّيِٰہ آڪٰྀہٰٰٖليِٰہنَِٰہٰيِٰہ 😹🙄   " ,
'reply_to_message_id'=>$message->message_id,
]);
}
if($text == "ها"){
bot( sendaudio ,[
 chat_id =>$chat_id, 
 audio =>"https://t.me/eee_o/33",
 reply_to_message_id =>$message->message_id, 
]);
}
if($text == "😡"){
bot( sendaudio ,[
 chat_id =>$chat_id, 
 audio =>"https://t.me/eee_o/33",
 reply_to_message_id =>$message->message_id, 
]);
}
if($text == "😔"){
bot( sendaudio ,[
 chat_id =>$chat_id, 
 audio =>"https://t.me/eee_o/30",
 reply_to_message_id =>$message->message_id, 
]);
}
if($text == "🚶💔"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"شبي كلبك مكسور يعمري ♥",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "🌚"){
bot( sendaudio ,[
 chat_id =>$chat_id, 
 audio =>"https://t.me/eee_o/36",
 reply_to_message_id =>$message->message_id, 
]);
}
if($text == "مرحبا"){
bot( sendaudio ,[
 chat_id =>$chat_id, 
 audio =>"https://t.me/eee_o/31",
 reply_to_message_id =>$message->message_id, 
]);
}
if($text == "بوت"){
bot( sendaudio ,[
 chat_id =>$chat_id, 
 audio =>"https://t.me/eee_o/38",
 reply_to_message_id =>$message->message_id, 
]);
}
if($text == "خاصك"){
bot( sendaudio ,[
 chat_id =>$chat_id, 
 audio =>"https://t.me/eee_o/39",
 reply_to_message_id =>$message->message_id, 
]);
}
if($text == "خاصج"){
bot( sendaudio ,[
 chat_id =>$chat_id, 
 audio =>"https://t.me/eee_o/40",
 reply_to_message_id =>$message->message_id, 
]);
}
if($text == "😹😹"){
bot( sendaudio ,[
 chat_id =>$chat_id, 
 audio =>"https://t.me/eee_o/41",
 reply_to_message_id =>$message->message_id, 
]);
}

if($text == "😹"){
bot( sendaudio ,[
 chat_id =>$chat_id, 
 audio =>"https://t.me/eee_o/41",
 reply_to_message_id =>$message->message_id, 
]);
}
if($text == "ضوجه"){
bot( sendaudio ,[
 chat_id =>$chat_id, 
 audio =>"https://t.me/eee_o/42",
 reply_to_message_id =>$message->message_id, 
]);
}
if($text == "نجبي"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"اكل خرا لك ",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "حزين"){
bot( sendaudio ,[
 chat_id =>$chat_id, 
 audio =>"https://t.me/UUV12/108",
 reply_to_message_id =>$message->message_id, 
]);
}
if($text == "يالله"){
bot( sendaudio ,[
 chat_id =>$chat_id, 
 audio =>"https://t.me/eee_o/43",
 reply_to_message_id =>$message->message_id, 
]);
}
if($text == "تمام"){
bot( sendaudio ,[
 chat_id =>$chat_id, 
 audio =>"https://t.me/eee_o/45",
 reply_to_message_id =>$message->message_id, 
]);
}
if($text == "احبج"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"حبتك حيه ام راسين نشالله",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "نرتبط"){
bot( sendaudio ,[
 chat_id =>$chat_id, 
 audio =>"https://t.me/eee_o/29",
 reply_to_message_id =>$message->message_id, 
]);
}
if($text == "مخنوك"){
bot( sendaudio ,[
 chat_id =>$chat_id, 
 audio =>"https://t.me/UUV12/80",
 reply_to_message_id =>$message->message_id, 
]);
}
if($text == "مخنوكة"){
bot( sendaudio ,[
 chat_id =>$chat_id, 
 audio =>"https://t.me/UUV12/79",
 reply_to_message_id =>$message->message_id, 
]);
}
if($text == 'تفعيل'){
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>"بشتغل بدون تفعيل حبي",
]);
}
if($text == "شكو ماكو"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"سلامتك",
'reply_to_message_id'=>$message->$message_id,
]);
}
if($text == "شلونك"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"تمام",
'reply_to_message_id'=>$message->$message_id,
]);
}
if($text == "تحبني"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"اعشقك",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "انجب"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"ديہ لك حہقيہرَرَ 🤡",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "جذاب"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"لا",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "ها"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"وجعا",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "ولي"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"دي",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "احبك"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"واني هم",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "حلو"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"ٱنـﮩـت الاحـلا",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "😎"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"يلا عود انته فد نعال",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "😱"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"خير خوفتني ",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "منو اكثر واحد"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"خالتك",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "منو اكثر واحد"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"وك اسف 🙁",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "ابن الكلب"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"عيب ابني 🔥",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "كواد"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"عيب 😨�🔥",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "حيدر"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" ؤرده مال الله هاذا",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "قندره"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"😂بحلكك😂",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "هلا"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"هـﮩـڵا بيـك 🌝❤️ ",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "العب"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"اوفُہ شتعلبّ حبيبي🙈🤍",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "ههه"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"دوم פـٍـٍبيبي",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "ههههه"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"دوم פـٍـٍبيبي",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "هههههه"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"دوم פـٍـٍبيبي",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "😍"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"عود فرحان الوصخ",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "☺️"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"اكعد راحه سمير",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "💋"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"انته غير سافل",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "ممكن نتعرف"){
bot( sendaudio ,[
 chat_id =>$chat_id, 
 audio =>"https://t.me/eee_o/29",
 reply_to_message_id =>$message->message_id, 
]);
}
if($text == "حلو"){
bot('sendaudio',[
'chat_id'=>$chat_id, 
'audio'=>"https://t.me/eee_o/46",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "☹️"){
bot('sendaudio',[
'chat_id'=>$chat_id, 
'audio'=>"https://t.me/eee_o/30",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "منورة"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"بنورك حياتي♥",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "🌝"){
bot('sendaudio',[
'chat_id'=>$chat_id, 
'audio'=>"https://t.me/eee_o/35",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "منور"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"لا مو منور بومة ",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "🚶" ){
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>" مٰ̲ہتَہَٰڪٰྀہٰٰٖليِٰہ شِٰہٰٰ؏ۤـہٰٰنَِٰہٰدڪٰྀہٰٰٖ تَہَٰمٰ̲ہشِٰہٰٰيِٰہ لخٰ̐ہآطر آللھہ 🤔" ,
'reply_to_message_id'=>$message->message_id,
]);
}
if($text == "هلو" or $text == "هلاو"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"هلوات عمري 🌚💛",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "🙈"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"عود يستحي الوصخ",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "😐"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"كبر لفك",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "🚶"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"وين جاي وين مولي",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "ضوجه"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"واني شعليه مثلا شسؤيلك",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "😻"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"ع شنو فرحان😒",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "😞"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"يمه فدوه ضايج الحلو🙊",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "بمكن علاقه"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"دي😹سؤي ؤيه خالتك ",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "حبيتك"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"شنو من اول رد حبيتني😹😹",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "مشتاقلك"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"انته ليش اجذب؟😹",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "مشتاقلج"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"😹بدء الزحف😹",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "شكد عمرك"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"اسف مرتبط😹",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "🙄"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"عدل عيؤنك لصير احول😐",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "هلو باي"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"شحسيت من هيج كتبت😹",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "خره"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" بـحـلكڪ😒💦 ",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "نعال"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" اخلاقك حبي😹😻",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "تعال"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" وين اجي😕 ",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "السلام عليكم"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" وعليكم السلام ورحمه حته الله ",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "مساء الخير"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" مساء النؤر حياتي ",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "صباح الخير"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" صباح الؤرد🙈 ",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "باي"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" سلمنه ع اهلك كلهم😹 ",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "تصبحون ع خير"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" وانته من اهلو ",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "هاي"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" هايات يرؤحي🙈😻",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "احم"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" اسـم الله😧اشربـ/ي دوة😓 ",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "وينك"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" موجود حبي☺️",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "اكلك"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" لتكول تره صطرتنه😹",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "اتفل"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" خووووختف💦💦",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "اموت عليك"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" 😻me to love🙈",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "شكو"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" لتدخل بما لا يعنيك😹🐸",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "اكلكم"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"😹لتكول😹",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "اوف"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" سلامتك من ال اوف",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "شونك"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" ع خودا😹 وانته",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "احجي عربي"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" لك بابا العربي ميرادله شي بس اقراه انكليزي😹",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "💔"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" ع شنو مكسؤر قلبك😒",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "تسلم"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" عياتو ولو😹🙈",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "شكرا"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" ولو😹",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "اجه العيد"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"😹 لعد متسبح😹",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "🌺"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" وانته عطرهه😻❤️",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "🐸"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" ساحف😹",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "😴"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" متولي تنام لعد😒😹",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "👳‍♀️"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" استر علينه شيخ😹😹",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "🤔"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" 😹بشنو دتفكر 😕",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "💦"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" بوجهك ياكلب بن الكلب",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "🤓"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" شدتحس😜",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "😏"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" عدل حلكك يول😂",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "انته بتحبني"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" 😹ولله ما ادري بس افكر😕",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "خاص"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" اجي وياكم😻",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "تكرهني"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"موووووت",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "اضحك"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"هههههههههههههه",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "ابجي"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"اهئ اهئ اهئ اهئ",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "من وين"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"بغداد",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "ع راسي"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"سالم راسك",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "فدوه"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"لخشمك يرؤحي",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "شنو احسن مسرح"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"كرياتين ووويلي يخبل",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "كرياتين"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"يخبل احسن نوعيه للشعر",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "موهير"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"يخلونه ما بعد الكرياتين حته الشعر يخبل يصير وسرح ولمعه بي ",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "عسل"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" مثلك😻",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "فديتك"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" فداك الي بالي😻",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "منو بالك"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" عباس ابو الغاز شبيك😻",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "استغفرلله"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" بركاتك مولاي♡♥️",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "راح اكفر"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"اشك حلكك اذا اسؤيهه",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "مداك"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" اجاوزك بسرعتي امري لله😻",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "امك شلونهه"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"مو البارحه جانت يم امك",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "ابوك شلونه"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" الحمدلله بخير😻",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "اكلج"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"داحسك دتزحف",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "تخليني"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" وانته وين عدك😻",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "مطي"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" حسن اخلاقك حب",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "نعل"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" بحلكك كبد",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "محمد"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" العشق♡♥️",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "سعدون"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"الغالي مالي♡♥️",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "بخير"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" عساك دوم انشالله",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "ليش احبك"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"♥️لان انته عشقي♥️",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "ليش اكرهك"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" لان ما احترمك😻",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "ضيف جديد"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"*اهلا وسهلا~♡",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "هلوو"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" يممممه هلا ب نبضي♡♥️😻",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "احبج"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" وليحب بلوه وين الله وقسمتي ترؤح يم عيؤؤنج الحلوه",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "شكد تحبني"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" بكد هوه الله بكد الكائنات",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "موال"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"☝🏿شكولي مال تحشيش ماخربها بلموال 😹❤️",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "صاكه"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" وينها خلي اكفش شعرها 😹😍 ",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "عشق"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" يمه اذوبــن 😌❤️ ",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "مرتي"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" يمه اذوبــن ♡♥️",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "ملابس"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" 🌚☝🏿 تريدهن من المول لو من باله ؟ ",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "مول"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" 😹☝🏿يريد يقطني ماشتريلك لوتموت ",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "باله"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>" 😹☝🏿 موحلوات عليك هم ماشتريلك
",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "اشو ماكو احد"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"موجودين حياتي-_-♥️",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "بعدك لو بطلت"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"بربك اكو واحد يعوف شغله -_-",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "ديي"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"انته اكبر زربه وبطل هاي اخلاقك زباله",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "اشو مختفي"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"وين مختفي بنلخرا غير موجود-_-",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "علو"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"اول شي كولهه عدل؟ثاني شي احجي",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "روجي"){
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>"ولك هاذا واحد سافل وسخيف لتحجي وياهه نصيحه مني ولله ع مودك -_-",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "😐💔"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"شبيك كال خلقتك",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "حبك"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"اعشقك يروح الروح",
'reply_to_message_id'=>$message->message_id, 
]);
} 
if($text == "اكرهك"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"بس مو بكدي ههه",
'reply_to_message_id'=>$message->message_id, 
]);
} 
if($text == "😴"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"ولي نام اذا هيج نعسان😹😹",
'reply_to_message_id'=>$message->message_id, 
]);
} 
if($text == "🙄"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"باوع عدل مطي😹😕",
'reply_to_message_id'=>$message->message_id, 
]);
} 
if($text == "حبيتج"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"لي اجذب انته وشبسرعه حبيتهه بن الزاحف😹😹",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "غنيلي"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"صوتي خره مو مال اغاني",
'reply_to_message_id'=>$message->message_id, 
]);
} 
if($text == "بوسني"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"ٲٳمٌـۧ﴿🌝💋﴾ـۛويِّحًهٍہ💕⇣ֆ ",
'reply_to_message_id'=>$message->message_id, 
]);
} 
if($text == "بوسه قويه"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"ٲٳمٌممممممممممممممممممـۧ﴿🌝💋﴾ـۛويِّحًهٍہ💕⇣ֆ ",
'reply_to_message_id'=>$message->message_id, 
]);
} 
if($text == "تحب روجي"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"لاع خلي ولي وصخ😹",
'reply_to_message_id'=>$message->message_id, 
]);
} 
if($text == "شغل ضوه"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"ميحتاج اشغله هوه انته شمعه ",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "علي المنصوري"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"الدنيا وش الدنيا لو شح الحبيب وويلي😍😍",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "اني منو"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"شمدريني متكلي تره اني بوت مو شخص 😹😕",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "ضوجه"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"ولي اطلع شعليه اني جاي يمي تكول ضوجه😹😐",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "تحبيني"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"ها بده الزحف مو😹😕",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "شغل مولده"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"بانزين مابيهه ولي جيب واشغلهه ",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "جبت بانزين"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"تدلل هسه اشغله بس لم من كل عضو الف مال بانزين😹😹",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "ايفون"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"وويلي كون عدي بس ولو زباله يرادله ايتونز😹😕",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "شكد متابعينج"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"مليارات قابل مثلك فاشل",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "اشكرك"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"ولو😍😹",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "شغل ثلاجه"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"شغلتهه ولدزني بعد تريد كوم انته فتهمت😡😹 ",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "شغل بلازما"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"تعبت ولرب كوم انته فدوه😹😻😻",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "شغل المروحه"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"😻شغلتهه استادي🙈😻",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "رتب الكروب راح يجي خطار"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"رتبته من الصبح كعدت ب 6😹😹🙈",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "🙈"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"عود يستحي وجه القرد الوصخ😹😹😹",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "زباله"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"لشبهني بيك فدوه",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "شسمج"){
bot('sendMessage',[
'chat_id'=>$chat_id, 
'text'=>"✧ دّلّـﮩﮧـؤٰ୭شـۿﮧّ😻🌸 ℡",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($text == "نعال"  ){
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=> " بـﮩـوجـهـڪ 😐😂" ,
'reply_to_message_id'=>$message->message_id,
]);
}
if($text == "حروح اسبح"  ){
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>" واخيراً 😹🌝"  ,
'reply_to_message_id'=>$message->message_id,
]);
}
if($text ==  "حروح اغسل" ){
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>" واخيراً 😹🌝"  ,
'reply_to_message_id'=>$message->message_id,
]);
}
if($text ==   "حروح اطب للحمام" ){
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>" واخيراً 😹🌝"  ,
'reply_to_message_id'=>$message->message_id,
]);
}
if($text ==   "حبيبتي" ){
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>" منو هاي 😱 تخوني 😔☹️"  ,
'reply_to_message_id'=>$message->message_id,
]);
}
if($text ==  "كبلت" ){
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>" بلخير 😂💔" ,
'reply_to_message_id'=>$message->message_id,
]);
}
if($text ==  "شكشك" ){
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>" موتتني شتريد " ,
'reply_to_message_id'=>$message->message_id,
]);
}
if($text ==  "عم شكشك" ){
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>" عيون شكشك " ,
'reply_to_message_id'=>$message->message_id,
]);
}
if($text == "البوت عاوي" ){
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>" اطردك ؟ 😒"  ,
'reply_to_message_id'=>$message->message_id,
]);
}
if($text == "حفلش"  ){
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=> " افلش راسك"  ,
'reply_to_message_id'=>$message->message_id,
]);
}
if($text == "حبيبي"  ){
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=> "مح محح تسلم" ,
'reply_to_message_id'=>$message->message_id,
]);
}
