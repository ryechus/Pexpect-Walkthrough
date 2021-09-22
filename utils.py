import pexpect


def print_lines(lines):
    for line in lines:
        print(line)


def try_2fa_codes(proc, count=0):
    verification_code = '123456'
    max_2fa_retries = 3  # limits the recursion to 3 times

    proc.sendline(verification_code)
    index = proc.expect([
        'Please enter the 6 digit code you received at.*:',
        'Please enter the 6 digit code:', pexpect.EOF])

    # If, after sending the verification code, we are prompted to enter the 6 digit code
    # then it means the code didn't work or something else happened. In that event we should
    # retry.
    if index in [0, 1] and count < max_2fa_retries:
        print(f'Incorrect 2FA verification code for')
        count += 1
        return try_2fa_codes(proc, count=count)
    elif index == 2:
        print(f'Sent verification code {verification_code}')
    elif count >= max_2fa_retries:
        raise Exception(f'No valid verification code found for')

    return proc
