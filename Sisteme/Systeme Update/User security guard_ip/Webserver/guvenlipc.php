<?php
	/* CONFIG */
	// MySQL
	$host = "127.0.0.1";					// MySQL Host
	$user = "wsrv";							// MySQL ID
	$pass = "123";							// MySQL PWD
	
	// Mail
	$mail_smtp_host = "smtp.gmail.com";		// SMTP Host
	$mail_smtp_port = 465;					// SMTP Port
	$mail_smtp_user = "xx@gmail.com";		// SMTP Mail user
	$mail_smtp_pass = "123";				// SMTP Mail pass
	
	$mail_from_adr	= 'koray@pasha37.de';
	$mail_title		= 'MyServer Bilgi servisi';
	$mail_subject	= 'Supheli Giris Bildirimi';
	
	error_reporting(0);
	// ---
	$conn = @mysqli_connect($host, $user, $pass, "account"); // Connect to MySQL Server
	
	if (!$conn)
		die ("web_sql_error"); // Check connection status
	
	// Set veriables
	$login = mysqli_real_escape_string($conn, $_GET['login']);
	$password = mysqli_real_escape_string($conn, $_GET['password']);
	$user_guard_code = mysqli_real_escape_string($conn, $_GET['guard_code']);
	$now_date = date("Y-m-d H:i:s");	// Now date
	$ip_info = $_SERVER['REMOTE_ADDR']; // Target user IP
	
	if (!$login || !$password)
		exit("");
	
	$check_sql = mysqli_query($conn, "SELECT * FROM `account` WHERE `login`='$login' AND `password`=PASSWORD('$password') ;"); // SQL Query
	$count = mysqli_num_rows($check_sql); // Length of query result
	
	if ($count != 1)
		exit("web_unknown_error"); // If not found or duplicate result
	
	$fetch = mysqli_fetch_array($check_sql); // Get php array from query result
	$real_name = $fetch['real_name']; // Him real name
	$email = $fetch['email']; // Him email
	$GUARD_IP = $fetch['guard_ip']; // Him old checked ip
	$GUARD_status = $fetch['guard_status'];   // Him guard status
	$GUARD_expire_date = $fetch['guard_date'];   // Him guard expire date
	$GUARD_code = $fetch['guard_code'];   // Him guard code
	
	if ($GUARD_IP == $ip_info || $GUARD_status == 0)
		exit("guard_is_ok"); // If guard status is ok or ip is same
	
	if ($GUARD_status == 2 || (time() - $GUARD_expire_date) < 3600 * 5){
		if ($user_guard_code == 0){
			exit("code_already_sended"); // If guard code sended as email
		}
		else{
			if ($user_guard_code == $GUARD_code)
				exit("code_is_valid"); // If guard is valid
			else
				exit("code_is_invalid");
		}
	}
	
	// Prepare mail stuff
	try {
		include_once('PHPMailer/class.phpmailer.php');
		$mail = new PHPMailer();
		
		$mail->SetFrom($mail_from_adr, $mail_title);
		$mail->Subject = $mail_subject;
		
		$mail->AddAddress($email);
		
		$code = rand(100000, 999999);
		
		$message	=	"Hello dear,  $real_name,<br/>"
		."Someone logged in to your account on $now_date.<br/>"
		."if you have not logged in, you can ignore this e-mail,<br/>"
		."If you are not attempting to login then please change your password and consider changing your email password as well to ensure your account security.<br/><br/>"
		
		."Here is the your activation code for login to account $login:<br/><br/>"
		
		." <b>$code</b><br/><br/>"
		

		."*** CAUTION: DO NOT ANSWER TO THIS E-MAIL *** <br/>"
		."This is an automatic e-mail sent from our support system.<br/>"
		
		."MyServer Management<br/>"
		."http://www.myserver.com<br/><br/><br/>"
		
		."The MyServer Support Team<br/>"
		."https://myserversupport.link<br/>";
		
		$mail->MsgHTML($message);
		
		$mail->IsSMTP();
		//$mail->SMTPDebug = 1;
		$mail->SMTPAuth = true;
		//$mail->SMTPSecure = 'ssl';
		$mail->SMTPSecure = 'tls';
		$mail->Host = $mail_smtp_host;
		$mail->Port = $mail_smtp_port;
		$mail->Username = $mail_smtp_user;
		$mail->Password = $mail_smtp_pass;
		
		if ($mail->Send()){
			echo "mail_is_sended"; // Send mail
			mysqli_query($conn, "UPDATE account SET guard_status=2, guard_code='$code', guard_date=UNIX_TIMESTAMP() WHERE login='$login'");
		}
		else{
			$fp = fopen ("errors.txt", "a+");  
			fwrite ($fp, "Error caught from: Mailer Error\n"); 
			fwrite ($fp, "Error: $mail->ErrorInfo\r\n");  
			fclose ($fp);
			echo "mailer_error";
			//echo "Mailer Error: " . $mail->ErrorInfo;
		}
	} catch (phpmailerException $e) {
		$fp = fopen ("errors.txt", "a+");  
		fwrite ($fp, "Error caught from: phpmailerException\n"); 
		fwrite ($fp, "Error: $e->errorMessage();\r\n");  
		fclose ($fp);
		echo "mailer_error";
		//echo $e->errorMessage(); //Pretty error messages from PHPMailer
	} catch (Exception $e) {
		$fp = fopen ("errors.txt", "a+");  
		fwrite ($fp, "Error caught from: Exception\n"); 
		fwrite ($fp, "Error: $e->getMessage();\r\n");  
		fclose ($fp);
		echo "mailer_error";
		//echo $e->getMessage(); //Boring error messages from anything else!
	}
	
	mysqli_close($conn); // Close connection
?>