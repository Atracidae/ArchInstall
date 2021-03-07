"""
Arch Install Part 1.
Assumes that drive 'nvme1n1p1' has been partitioned.  No need to format.
"""
import time
import os

# Start Timer.
start = time.time()

# Variables.
partition_root = '/dev/sdc2'
partition_boot = '/dev/sdc1'
boot_dir = '/mnt/boot/efi'

# Some initial settings and starting up cfdisk.
os.system("timedatectl set-ntp true")
os.system("cfdisk /dev/sdc")

# Format partitions.  Assumes User made the Correct partitions in the correct spot..
os.system(f"mkfs.fat -F32 {partition_boot}")
os.system(f"mkfs.ext4 {partition_root}")

# Make Directories.
os.system("mkdir /mnt/boot")
os.system(f"mkdir {boot_dir}")

# Mount partitions to proper directories.
os.system(f"mount {partition_root} /mnt")
os.system(f"mount {partition_boot} {boot_dir}")


# Inform User of progress.
print('\nPartitions formatted and mounted; base packages installing now.\n')
print('Sleeping for 3 seconds.')
time.sleep(3)

# Download and Write base to disk.
os.system("pacstrap /mnt base")
os.system("genfstab -U /mnt >> /mnt/etc/fstab")

# Copy downloaded git contents to new home directory for use after arch-chroot.
os.system('cp ArchInstall /mnt/home/ -r')


# Print time taken and other info.
end = time.time()
total_time = end - start
print(f'Finished for now!\n....\nThis process took {round(total_time * .0001, 5)} minutes.')
print('arch-chroot into /mnt')
print('Then Run part 2.')
exit()
# Could I perhaps use my existing functions to do this next part with a little bit of modification?

