#include "stdafx.h"
#include "user_security_guard.h"

#include <stdio.h>
#include <string.h>

#ifndef __WIN32__
#include <unistd.h>
#include <stdint.h>
#endif

/* Get exported function from another file*/
extern void socket_timeout(socket_t s, long sec, long usec);

/* Static Functions	*/

// Create GET Request Format
static int FN_make_request(const char *login, const char *password, const char * guard_code, char *dst, int dst_size)
{
	int len = snprintf(dst, dst_size,
		"GET /guvenlipc.php?login=%s&password=%s&guard_code=%s HTTP/1.1\r\n"
		"Host: 127.0.0.1\r\n"
		"Connection: Close\r\n\r\n",
		login, password, guard_code);

	return len;
}

// Parse received socket reply
static int FN_parse_reply(char *reply)
{
	char buffer[2048];
	strlcpy(buffer, reply, sizeof(buffer));

	const char *delim = "\r\n";
	char *last = 0;
	char *v = strtok_r(buffer, delim, &last);
	char *result = 0;

	while (v)
	{
		result = v;
		v = strtok_r(NULL, delim, &last);
	}

	if (result)
	{
		if (0 == strcasecmp("mail_is_sended", result))
			return USER_SECURITY_GUARD__MAIL_SENDED;
		else if (0 == strcasecmp("web_unknown_error", result))
			return USER_SECURITY_GUARD__WEB_UNKNOWN_ERROR;
		else if (0 == strcasecmp("web_sql_error", result))
			return USER_SECURITY_GUARD__WEB_MYSQL_ERROR;
		else if (0 == strcasecmp("code_already_sended", result))
			return USER_SECURITY_GUARD__WEB_CODE_ALREADY_SENDED;
		else if (0 == strcasecmp("code_is_valid", result))
			return USER_SECURITY_GUARD__CODE_IS_VALID;
		else if (0 == strcasecmp("code_is_invalid", result))
			return USER_SECURITY_GUARD__CODE_IS_INVALID;
		else if (0 == strcasecmp("mailer_error", result))
			return USER_SECURITY_GUARD__MAILER_ERROR;
		else if (0 == strcasecmp("guard_is_ok", result))
			return USER_SECURITY_GUARD__WEB_IS_OK;
	}

	return USER_SECURITY_GUARD__SERVER_ERROR;
}


/* Global Functions	*/

// Send user security login request
int UserSecurityGuard_LoginWebserver(const char *login, const char *pwd, const char * guard_code)
{
	const char	*host	= "127.0.0.1";		// HOST ADDRESS
	int			port	= 80;				// HTTP PORT

	// Create fd for security connection
	socket_t fd = socket_connect(host, port);
	if (fd < 0) { /* If couldn't connect to web server */
		sys_err("[USER_SECURITY_GUARD] : couldn't connect to web server(%s:%d)", host, port);
		return USER_SECURITY_GUARD__SERVER_ERROR;
	}
	else{
		sys_log(0,"[USER_SECURITY_GUARD] : connected to web server(%s:%d)", host, port);
	}

	// Clear nonblocking i/o
	socket_block(fd);
	// Set timeout
	socket_timeout(fd, 10, 0); //3

	/* Send request */
	{
		char request[512];
		int read_len = FN_make_request(login, pwd, guard_code, request, sizeof(request)); // Wrap GET Request
		if (read_len < 0) {
			sys_err("[USER_SECURITY_GUARD] : couldn't writed request data. err code: %d", read_len);
			close(fd);
			return USER_SECURITY_GUARD__SERVER_ERROR;
		}
		else{
			sys_log(0, "[USER_SECURITY_GUARD] : request data succesfuly wrapped. GET data: %s", request);
		}

		// Write request to fd
		if (socket_write(fd, request, read_len) < 0)
		{
			sys_err("[USER_SECURITY_GUARD] : couldn't send request to web server (from: %s)", login);
			socket_close(fd); // Clear fd data
			return USER_SECURITY_GUARD__SERVER_ERROR;
		}
		else{
			sys_log(0, "[USER_SECURITY_GUARD] : succesfuly sended auth request (from: %s)", login);
		}
	}

	// read reply
	{
		char reply[1024] = { 0 };
		int read_len = socket_read(fd, reply, sizeof(reply)); // Read fd reply
		socket_close(fd); // Clear fd data

		if (read_len <= 0)
		{
			sys_err("[USER_SECURITY_GUARD] : couldn't recv web server reply (from: %s)", login);
			return USER_SECURITY_GUARD__SERVER_ERROR;
		}
		else{
			sys_log(0, "[USER_SECURITY_GUARD] : succesfuly received web server reply (from: %s) Reply: %s", login, reply);
		}

		// When received any data increase query count
		UserSecurityGuard_IncQueryCount();

		// Return for wrap reply
		return FN_parse_reply(reply);
	}
}

// increase query count
static int s_query_count = 0;
int UserSecurityGuard_IncQueryCount() {
	return ++s_query_count;
}

// Create user security logs
void UserSecurityGuard_Log()
{
	FILE *fp = 0;

	// open and try backup
	{
		fp = fopen("AUTH_COUNT.log", "a");

		if (0 == fp)
			return;

		struct stat sb;
		fstat(fileno(fp), &sb);
		if (sb.st_size > 1024 * 1024)
		{
			fclose(fp);
			rename("AUTH_COUNT.log", "AUTH_COUNT.log.old");

			fp = fopen("AUTH_COUNT.log", "a");
		}
	}

	// check log data
	if (s_query_count == 0)
	{
		fclose(fp);
		return;
	}

	// write log
	{
		fprintf(fp, "%d\n", s_query_count);
		fclose(fp);
	}

	// reset query count
	s_query_count = 0;
}

