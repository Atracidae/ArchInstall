"""
Arch Install Part 2.
Do Not Run This Program!
"""

import os
import time


def locale():
    """ hmm """
    conf_list = [
        'LANG=en_US.UTF-8\n',  # noqa
        'LC_CTYPE=en_US.UTF-8\n',  # noqa
        'LC_NUMERIC=en_US.UTF-8\n',  # noqa
        'LC_TIME=en_US.UTF-8\n',  # noqa
        'LC_COLLATE=en_US.UTF-8\n',  # noqa
        'LC_MONETARY=en_US.UTF-8\n',  # noqa
        'LC_MESSAGES="en_US.UTF-8"\n',  # noqa
        'LC_PAPER="en_US.UTF-8"\n',  # noqa
        'LC_NAME="en_US.UTF-8"\n',  # noqa
        'LC_ADDRESS="en_US.UTF-8"\n',  # noqa
        'LC_TELEPHONE="en_US.UTF-8"\n',  # noqa
        'LC_MEASUREMENT=en_GB.UTF-8\n',  # noqa
        'LC_IDENTIFICATION="en_US.UTF-8"\n',  # noqa
        'LC_ALL=',  # noqa
    ]
    locale_gen_file = "/etc/locale.gen"
    locale_conf_file = "/etc/locale.conf"
    os.system("ln -sf /usr/share/zoneinfo/America/New_York")
    os.system("hwclock --systohc")
    os.system(f'rm {locale_gen_file}')
    os.system(f'rm {locale_conf_file}')
    os.system(f'cp locale.gen {locale_gen_file}')
    os.system("locale-gen")
    os.system(f'touch {locale_conf_file}')
    with open(locale_conf_file, 'w') as file:
        for i in conf_list:
            file.write(i)

def net():

    host_name = input('Please Enter a HostName for system: >>  ')
    with open('/etc/hostname', 'x') as f3:
        f3.write(host_name)
    with open('/etc/hosts', 'a') as f4:
        f4.write(f"127.0.0.1     localhost\n")
        f4.write(f"::1           localhost\n")
        f4.write(f"127.0.1.1     {host_name}.localdomain    {host_name}")

def install_packages():
    package_list = [
        'linux linux-headers linux-firmware',
        'python3',
        'dhcpcd grub efibootmgr git',
        'sudo nano vim vi man',
        'amd-ucode mesa nvidia nvidia-utils base-devel',
        'networkmgr wpa_supplicant wireless_tools netctl dialog',
    ]

    for packages in package_list:
        os.system(f'pacman -S {packages}')


    os.system("systemctl enable dhcpcd")
    os.system("systemctl enable NetworkManager")  # Caps are necessary.

    # If installing linux and linux-lts, running this command once for each instance of kernel is needed.
    os.system("mkinitcpio -p linux")

def create_users():
    # Create passwd for root.
    print('enter pw for root')
    os.system("passwd")

    # Create Spider
    print('enter pw for spider')
    os.system('useradd -m -g users -G wheel spider')
    os.system('passwd spider')

    # Create Alpha
    print('enter pw for alpha')
    os.system('useradd -m -g users -G wheel alpha')
    os.system('passwd alpha')

def grub():
    os.system("grub-install --target=x86_64-efi  --bootloader-id=grub_uefi --recheck")
    os.system('mkdir /boot/grub/locale')
    os.system(r'cp /usr/share/locale/en\@quot/LC_MESSAGES/grub.mo /boot/grub/locale/en.mo')
    os.system(r'grub-mkconfig -o /boot/grub/grub.cfg')







if __name__ == '__main__':
    print('Starting in .5')
    time.sleep(.5)

    # Run Functions.
    locale()
    net()
    install_packages()
    create_users()
    grub()
    os.system('rm ArchInstall /mnt/home/ -r')

    print("\n\nFinished!\nPlease remove installation media and restart.")

    print(""" 
    Still need to do the following:
    add User
    edit visudo
    set up sudo
    set up grub
    enable things
    """)

