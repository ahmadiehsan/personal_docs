# Fault-Tolerant (Resilient)

## Description

The things that can go wrong are called faults, and systems that anticipate faults and can cope with them are called fault-tolerant or resilient.

Note that a fault is not the same as a failure.
A fault is usually defined as one component of the system deviating from its spec, whereas a failure is when the system as a whole stops providing the required service to the user.

**It is usually best to design fault-tolerance mechanisms that prevent faults from causing failures.**

## Hardware Faults

Hard disks are reported as having a mean time to failure (MTTF) of about 10 to 50 years.
Thus, on a storage cluster with 10,000 disks, we should expect on average one disk to die per day.
