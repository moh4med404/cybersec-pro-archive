# Cybersecurity 101 
---
# Wireshark Basics

Wireshark is an open-source, cross-platform network packet analyser tool capable of sniffing and investigating live traffic and inspecting packet captures (PCAP). It is commonly used as one of the best packet analysis tools. In this room, we will look at the basics of Wireshark and use it to perform fundamental packet analysis.

### Use Cases

Wireshark is one of the most potent traffic analyser tools available in the wild. There are multiple purposes for its use:

- Detecting and troubleshooting network problems, such as network load failure points and congestion.
- Detecting security anomalies, such as rogue hosts, abnormal port usage, and suspicious traffic.
- Investigating and learning protocol details, such as response codes and payload data. 

**Note**: Wireshark is not an Intrusion Detection System (IDS). It only allows analysts to discover and investigate the packets in depth. It also doesn't modify packets; it reads them. Hence, detecting any anomaly or network problem highly relies on the analyst's knowledge and investigation skills.


### GUI and Data

Wireshark GUI opens with a single all-in-one page, which helps users investigate the traffic in multiple ways. At first glance, five sections stand out.

| **Component**              | **Description**                                                                                                                                              |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Toolbar**                 | The main toolbar contains multiple menus and shortcuts for packet sniffing and processing, including filtering, sorting, summarising, exporting, and merging. |
| **Display Filter Bar**     | The main query and filtering section.                                                                                                                        |
| **Recent Files**           | List of the recently investigated files. You can recall listed files with a double-click.                                                                     |
| **Capture Filter and Interfaces** | Capture filters and available sniffing points (network interfaces).  The network interface is the connection point between a computer and a network. The software connection (e.g., lo, eth0 and ens33) enables networking hardware. |
| **Status Bar**             | Tool status, profile, and numeric packet information.                                                                                                        |

The below picture shows Wireshark's main window. The sections explained in the table are highlighted. Now open the Wireshark and go through the walkthrough.

<img src="./Cybersecurity_101_screenshots/wireshark01.jpg" width="800" alt="Screenshot 1"> <br>


### Loading PCAP Files

The above picture shows Wireshark's empty interface. The only available information is the recently processed  "http1.cap" file. Let's load that file and see Wireshark's detailed packet presentation. Note that you can also use the **"File"** menu, dragging and dropping the file, or double-clicking on the file to load a pcap.

<img src="./Cybersecurity_101_screenshots/wireshark02.jpg" width="800" alt="Screenshot 2"> <br>

Now, we can see the processed filename, detailed number of packets and packet details. Packet details are shown in three different panes, which allow us to discover them in different formats. 

| **Pane**              | **Description**                                                                                                                                                 |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Packet List Pane**  | Displays a summary of each packet, including source and destination addresses, protocol, and packet information. Click on a packet to inspect its details.       |
| **Packet Details Pane** | Shows a detailed protocol breakdown of the selected packet. Each protocol layer is expanded hierarchically for deeper inspection.                               |
| **Packet Bytes Pane** | Provides a hex and decoded ASCII representation of the selected packet. Highlights corresponding bytes when sections are selected in the details pane.           |


### Wireshark Packet Colouring and Visualization

Wireshark enhances packet analysis by **colouring packets** based on different **protocols and conditions**. This feature allows analysts to **quickly identify anomalies and key events** in traffic captures.

#### 🔍 Quick Glance Value
- Most packets may appear **green by default** in the interface, indicating standard traffic.
- Colouring helps **visually distinguish** between protocols or abnormal events.
- A great aid during analysis for **tracking specific traffic patterns** or **issues**.

---

#### 🎨 Types of Packet Colouring in Wireshark

| **Colouring Type**      | **Description**                                                                                                 |
|-------------------------|-----------------------------------------------------------------------------------------------------------------|
| **Temporary Rules**     | Exist **only during the current session**. These are not saved after closing Wireshark.                        |
| **Permanent Rules**     | Saved to the **user's profile** and persist between sessions. Configured via menus or preference files.         |

---

#### 📂 How to Manage Colouring Rules

| **Action**                              | **Menu Path / Method**                                                                                   |
|----------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Create Permanent Colouring Rule        | `Right-click on packet` → **Colorize Conversation** OR `View` → **Coloring Rules...**                    |
| Activate/Deactivate Colouring          | `View` → **Colorize Packet List**                                                                         |
| Temporary Packet Colouring             | `Right-click on packet` → **Colorize Conversation** OR `View` → **Conversation Filter** *(See TASK-5)*    |

---

#### 🧠 Coming Up Next
We'll explore how to use **display filters** and create **custom colour rules** for identifying events of interest in **TASK-5**.

The default permanent colouring is shown below.

<img src="./Cybersecurity_101_screenshots/wireshark03.jpg" width="800" alt="Screenshot 3"> <br>

## 🦈 STraffic Sniffing

Wireshark provides an intuitive set of control buttons to manage packet capturing:

#### 🎛️ Capture Control Buttons

| **Button**             | **Function**                                                                 |
|------------------------|------------------------------------------------------------------------------|
| 🔵 **Blue Shark Button** | Starts **network sniffing** (begins capturing live traffic).                  |
| 🔴 **Red Button**        | Stops the current **packet capture** session.                                 |
| 🟢 **Green Button**      | **Restarts** packet capturing, useful for clearing and starting fresh capture. |


#### 📊 Status Bar Information

The **status bar** at the bottom of Wireshark displays:

- The **active sniffing interface** (e.g., `eth0`, `Wi-Fi`).
- The **number of packets captured** in real time.
- Any **capture-related messages or errors**.

> ✅ Tip: Always verify the selected interface before starting capture to ensure you’re sniffing the right network segment.

<img src="./Cybersecurity_101_screenshots/wireshark04.jpg" width="800" alt="Screenshot 4"> <br>

## 🔗 Merging PCAP Files in Wireshark

Wireshark allows you to **combine two `.pcap` files into a single file**, which is useful for aggregating data from multiple capture sessions.

### 📂 How to Merge PCAP Files

1. Go to **`File` → `Merge...`**
2. Select the second `.pcap` file you want to merge with the one currently open.
3. Wireshark will display the **total number of packets** in the file you selected.
4. Click **`Open`** to merge the selected file with the current one.
5. After merging, **save the merged file** using `File → Save As` before analyzing or editing.


### ⚠️ Important Notes

- The merged file is **not saved automatically** — you must manually save it.
- The **merged `.pcap`** contains packets from both files, typically sorted by **timestamp** (unless disabled).
- Useful for creating **comprehensive traffic captures** from segmented logs.

> ✅ Tip: Use consistent capture interfaces and clock synchronization when merging multiple files for accurate analysis.

## 🗂️ Viewing PCAP File Details in Wireshark

When analyzing multiple `.pcap` files, it's essential to access file-specific information for **identification, classification, and prioritization**.

### 📋 Why File Details Matter

- Helps identify the **origin and content** of the file.
- Useful for **comparing capture times**, **interfaces**, and **network environments**.
- Allows tracking of **hash values**, **comments**, and **statistical metadata**.


### 🔍 How to View File Details

| **Method**                                | **Description**                                                                 |
|-------------------------------------------|---------------------------------------------------------------------------------|
| `Statistics → Capture File Properties`     | Opens a window displaying all metadata related to the current `.pcap` file.     |
| Click the **PCAP icon** (📄)               | Located at the **bottom-left** corner of Wireshark's window for quick access.   |


### 🧾 Information Available

- **File Hash** (SHA-256, useful for verification)
- **Capture Start/End Time**
- **Capture File Comments**
- **Capture Interface Name**
- **Number of Packets**
- **Packet Size Statistics**
- **Dropped Packets (if available)**

> ✅ Tip: Add a descriptive **comment** to your capture files to make future identification easier, especially during collaborative investigations.

---

# Packet Dissection

Packet dissection is also known as protocol dissection, which investigates packet details by decoding available protocols and fields. Wireshark supports a long list of protocols for dissection, and you can also write your dissection scripts.

**Note:** This section covers how Wireshark uses OSI layers to break down packets and how to use these layers for analysis. It is expected that you already have background knowledge of the OSI model and how it works. 

### 🧩 Packet Details in Wireshark

When you click on a packet in the **Packet List Pane**, the **Packet Details Pane** displays a structured breakdown of the packet's contents.

- ✅ **Single-click** a packet: Shows its details in the pane below.
- ✅ **Double-click** a packet: Opens the packet details in a **separate window**.

---

#### 🌐 OSI Model Layers in a Packet

Each packet in Wireshark is dissected according to the **OSI model**. Most packets contain between **5 to 7 layers**, depending on the protocol and encapsulation.

#### Example: Layers in an HTTP Packet
| **Layer**         | **Description**                                         |
|-------------------|---------------------------------------------------------|
| **Layer 1: Physical**   | Not shown directly in Wireshark (handled by hardware).    |
| **Layer 2: Data Link**  | e.g., Ethernet II – Contains MAC addresses.               |
| **Layer 3: Network**    | e.g., IPv4 or IPv6 – Contains IP addressing info.         |
| **Layer 4: Transport**  | e.g., TCP or UDP – Handles ports and sequencing.          |
| **Layer 5: Session**    | Often abstract; managed through TCP state tracking.       |
| **Layer 6: Presentation** | Optional – Wireshark interprets encoding formats (e.g., TLS). |
| **Layer 7: Application** | e.g., HTTP, DNS – Actual data payload and protocol commands. |

---

#### 🔍 Practical Use

By expanding each layer in the Packet Details Pane, you can:
- Inspect **headers**, **flags**, and **payloads**
- **Follow TCP streams** to see entire conversations
- Identify issues like **retransmissions**, **protocol violations**, or **malicious payloads**

 The picture below shows viewing packet number 27.

<img src="./Cybersecurity_101_screenshots/wireshark05.jpg" width="800" alt="Screenshot 5"> <br>

Each time you click a detail, it will highlight the corresponding part in the packet bytes pane.

<img src="./Cybersecurity_101_screenshots/wireshark06.jpg" width="800" alt="Screenshot 6"> <br>

Let's have a closer view of the details pane.

<img src="./Cybersecurity_101_screenshots/wireshark07.jpg" width="800" alt="Screenshot 7"> <br>

We can see seven distinct layers to the packet: frame/packet, source [MAC], source [IP], protocol, protocol errors, application protocol, and application data. Below we will go over the layers in more detail.

1. **The Frame (Layer 1):** This will show you what frame/packet you are looking at and details specific to the Physical layer of the OSI model.

<img src="./Cybersecurity_101_screenshots/wireshark08.jpg" width="800" alt="Screenshot 8"> <br>

2. **Source [MAC] (Layer 2**): This will show you the source and destination MAC Addresses; from the Data Link layer of the OSI model.

<img src="./Cybersecurity_101_screenshots/wireshark09.jpg" width="800" alt="Screenshot 9"> <br>

3. **Source [IP] (Layer 3)**: This will show you the source and destination IPv4 Addresses; from the Network layer of the OSI model.

<img src="./Cybersecurity_101_screenshots/wireshark10.jpg" width="800" alt="Screenshot 10"> <br>

4. **Protocol (Layer 4)**: This will show you details of the protocol used (UDP/TCP) and source and destination ports; from the Transport layer of the OSI model.

<img src="./Cybersecurity_101_screenshots/wireshark11.jpg" width="800" alt="Screenshot 11"> <br>

5. **Protocol Errors**: This continuation of the 4th layer shows specific segments from TCP that needed to be reassembled.

<img src="./Cybersecurity_101_screenshots/wireshark12.jpg" width="800" alt="Screenshot 12"> <br>

6. **Application Protocol (Layer 5)**: This will show details specific to the protocol used, such as HTTP, FTP,  and SMB. From the Application layer of the OSI model.

<img src="./Cybersecurity_101_screenshots/wireshark13.jpg" width="800" alt="Screenshot 13"> <br>

7. **Application Data**: This extension of the 5th layer can show the application-specific data.

<img src="./Cybersecurity_101_screenshots/wireshark14.jpg" width="800" alt="Screenshot 14"> <br>

---

# Packet Navigation

### Packet Numbers

Wireshark calculates the number of investigated packets and assigns a unique number for each packet. This helps the analysis process for big captures and makes it easy to go back to a specific point of an event. 

<img src="./Cybersecurity_101_screenshots/wireshark15.jpg" width="800" alt="Screenshot 15"> <br>


### Go to Packet

Packet numbers do not only help to count the total number of packets or make it easier to find/investigate specific packets. This feature not only navigates between packets up and down; it also provides in-frame packet tracking and finds the next packet in the particular part of the conversation. You can use the "Go" menu and toolbar to view specific packets.

<img src="./Cybersecurity_101_screenshots/wireshark16.jpg" width="800" alt="Screenshot 16"> <br>

### Find Packets

Apart from packet number, Wireshark can find packets by packet content. You can use the **"Edit --> Find Packet"** menu to make a search inside the packets for a particular event of interest. This helps analysts and administrators to find specific intrusion patterns or failure traces.

There are two crucial points in finding packets. The first is knowing the input type. This functionality accepts four types of inputs (Display filter, Hex, String and Regex). String and regex searches are the most commonly used search types. Searches are case insensitive, but you can set the case sensitivity in your search by clicking the radio button.

The second point is choosing the search field. You can conduct searches in the three panes (packet list, packet details, and packet bytes), and it is important to know the available information in each pane to find the event of interest. For example, if you try to find the information available in the packet details pane and conduct the search in the packet list pane, Wireshark won't find it even if it exists.

<img src="./Cybersecurity_101_screenshots/wireshark17.jpg" width="900" alt="Screenshot 17"> <br>

### Mark Packets
Marking packets is another helpful functionality for analysts. You can find/point to a specific packet for further investigation by marking it. It helps analysts point to an event of interest or export particular packets from the capture. You can use the **"Edit"** or the "right-click" menu to mark/unmark packets.

Marked packets will be shown in black regardless of the original colour representing the connection type. Note that marked packet information is renewed every file session, so marked packets will be lost after closing the capture file. 

<img src="./Cybersecurity_101_screenshots/wireshark18.jpg" width="900" alt="Screenshot 18"> <br>

### Packet Comments

Similar to packet marking, commenting is another helpful feature for analysts. You can add comments for particular packets that will help the further investigation or remind and point out important/suspicious points for other layer analysts. Unlike packet marking, the comments can stay within the capture file until the operator removes them.

<img src="./Cybersecurity_101_screenshots/wireshark19.jpg" width="900" alt="Screenshot 19"> <br>


### Export Packets

Capture files can contain thousands of packets in a single file. As mentioned earlier, Wireshark is not an IDS, so sometimes, it is necessary to separate specific packages from the file and dig deeper to resolve an incident. This functionality helps analysts share the only suspicious packages (decided scope). Thus redundant information is not included in the analysis process. You can use the **"File"** menu to export packets.

<img src="./Cybersecurity_101_screenshots/wireshark20.jpg" width="900" alt="Screenshot 20"> <br>

### Export Objects (Files)

Wireshark can extract files transferred through the wire. For a security analyst, it is vital to discover shared files and save them for further investigation. Exporting objects are available only for selected protocol's streams (DICOM, HTTP, IMF, SMB and TFTP).


<img src="./Cybersecurity_101_screenshots/wireshark21.jpg" width="900" alt="Screenshot 21"> <br>

### Time Display Format

Wireshark lists the packets as they are captured, so investigating the default flow is not always the best option. By default, Wireshark shows the time in "Seconds Since Beginning of Capture", the common usage is using the UTC Time Display Format for a better view. You can use the **"View --> Time Display Format"** menu to change the time display format.

<img src="./Cybersecurity_101_screenshots/wireshark22.jpg" width="900" alt="Screenshot 22"> <br>
<img src="./Cybersecurity_101_screenshots/wireshark23.jpg" width="900" alt="Screenshot 23"> <br>

### Expert Info

Wireshark also detects specific states of protocols to help analysts easily spot possible anomalies and problems. Note that these are only suggestions, and there is always a chance of having false positives/negatives. Expert info can provide a group of categories in three different severities. Details are shown in the table below.

<img src="./Cybersecurity_101_screenshots/wireshark24.jpg" width="900" alt="Screenshot 24"> <br>

Frequently encountered information groups are listed in the table below. You can refer to Wireshark's official documentation for more information on the expert information entries.

<img src="./Cybersecurity_101_screenshots/wireshark25.jpg" width="900" alt="Screenshot 25"> <br>

You can use the **"lower left bottom section"** in the status bar or **"Analyse --> Expert Information"** menu to view all available information entries via a dialogue box. It will show the packet number, summary, group protocol and total occurrence.

<img src="./Cybersecurity_101_screenshots/wireshark26.jpg" width="900" alt="Screenshot 26"> <br>

---

# Packet Filtering

Wireshark has a powerful filter engine that helps analysts to narrow down the traffic and focus on the event of interest. Wireshark has two types of filtering approaches: capture and display filters. Capture filters are used for **"capturing"** only the packets valid for the used filter. Display filters are used for **"viewing"** the packets valid for the used filter. We will discuss these filters' differences and advanced usage in the next room. Now let's focus on basic usage of the display filters, which will help analysts in the first place.

Filters are specific queries designed for protocols available in Wireshark's official protocol reference. While the filters are only the option to investigate the event of interest, there are two different ways to filter traffic and remove the noise from the capture file. The first one uses queries, and the second uses the right-click menu. Wireshark provides a powerful GUI, and there is a golden rule for analysts who don't want to write queries for basic tasks: **"If you can click on it, you can filter and copy it"**.

## Apply as Filter

This is the most basic way of filtering traffic. While investigating a capture file, you can click on the field you want to filter and use the "right-click menu" or "**Analyse --> Apply as Filter"** menu to filter the specific value. Once you apply the filter, Wireshark will generate the required filter query, apply it, show the packets according to your choice, and hide the unselected packets from the packet list pane. Note that the number of total and displayed packets are always shown on the status bar.

<img src="./Cybersecurity_101_screenshots/wireshark27.jpg" width="900" alt="Screenshot 27"> <br>

## Conversation Filter

When you use the "Apply as a Filter" option, you will filter only a single entity of the packet. This option is a good way of investigating a particular value in packets. However, suppose you want to investigate a specific packet number and all linked packets by focusing on IP addresses and port numbers. In that case, the "Conversation Filter" option helps you view only the related packets and hide the rest of the packets easily. You can use the"right-click menu" or **"Analyse --> Conversation Filter"** menu to filter conversations.

<img src="./Cybersecurity_101_screenshots/wireshark28.jpg" width="900" alt="Screenshot 28"> <br>

## Colourise Conversation

This option is similar to the "Conversation Filter" with one difference. It highlights the linked packets without applying a display filter and decreasing the number of viewed packets. This option works with the "Colouring Rules" option ad changes the packet colours without considering the previously applied colour rule. You can use the "right-click menu" or **"View --> Colourise Conversation"** menu to colourise a linked packet in a single click. Note that you can use the **"View --> Colourise Conversation --> Reset Colourisation"** menu to undo this operation.

<img src="./Cybersecurity_101_screenshots/wireshark29.jpg" width="900" alt="Screenshot 29"> <br>

## Prepare as Filter 

Similar to "Apply as Filter", this option helps analysts create display filters using the "right-click" menu. However, unlike the previous one, this model doesn't apply the filters after the choice. It adds the required query to the pane and waits for the execution command (enter) or another chosen filtering option by using the **".. and/or.."** from the "right-click menu".

<img src="./Cybersecurity_101_screenshots/wireshark30.jpg" width="900" alt="Screenshot 30"> <br>

## Apply as Column

By default, the packet list pane provides basic information about each packet. You can use the "right-click menu" or **"Analyse --> Apply as Column"** menu to add columns to the packet list pane. Once you click on a value and apply it as a column, it will be visible on the packet list pane. This function helps analysts examine the appearance of a specific value/field across the available packets in the capture file. You can enable/disable the columns shown in the packet list pane by clicking on the top of the packet list pane.

<img src="./Cybersecurity_101_screenshots/wireshark31.jpg" width="900" alt="Screenshot 31"> <br>

## Follow Stream

Wireshark displays everything in packet portion size. However, it is possible to reconstruct the streams and view the raw traffic as it is presented at the application level. Following the protocol, streams help analysts recreate the application-level data and understand the event of interest. It is also possible to view the unencrypted protocol data like usernames, passwords and other transferred data.

You can use the"right-click menu" or  **"Analyse --> Follow TCP/UDP/HTTP Stream"** menu to follow traffic streams. Streams are shown in a separate dialogue box; packets originating from the server are highlighted with blue, and those originating from the client are highlighted with red.

<img src="./Cybersecurity_101_screenshots/wireshark32.jpg" width="900" alt="Screenshot 32"> <br>

Once you follow a stream, Wireshark automatically creates and applies the required filter to view the specific stream. Remember, once a filter is applied, the number of the viewed packets will change. You will need to use the **"X button"** located on the right upper side of the display filter bar to remove the display filter and view all available packets in the capture file. 

---
> **Note:** These notes document hands-on learning from the TryHackMe *Cybersecurity 101* path. The exercises cover fundamental cybersecurity topics, including Linux basics, networking concepts, and web technologies. This document is intended for personal learning, revision, and ethical skill development. All screenshots, commands, and actions are for educational purposes only.  
> — Compiled by moh4med404 | Curious Mind | Cybersecurity Enthusiast
