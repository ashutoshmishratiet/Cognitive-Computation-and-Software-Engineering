# Cognitive & Emotional Performance System - Methodology Flowcharts

This document contains comprehensive flowchart diagrams for the Admin and User methodologies used in the system. These flowcharts can be used in research projects, dissertations, and technical documentation.

---

## 1. Admin Methodology Flowchart

The Admin flowchart illustrates the complete workflow for administrators managing data, creating analyses, and publishing results for users.

### Admin Workflow Components:

**A. Authentication**
- Register/Login to System
- Access Admin Dashboard

**B. Data Management**
- Upload Data Files
- Validate File Format
- Save File to System
- Deactivate Previous Files
- Data Manager Interface
  - Activate Dataset
  - Archive Files
  - Download Dataset

**C. Analysis Creation (Paper-Compliant)**
- Quick Analysis Creation
- Select Active Data File
- Validate Data Against Schema
- Compute Metrics:
  - TI (Technical Index)
  - NTI (Non-Technical Index)
  - CMI_P (Comprehensive Metrics Index)
- Generate Summary Statistics:
  - CUI (Cognitive Understanding Index)
  - CDI (Cognitive Debugging Index)
  - CCI (Cognitive Completion Index)
  - PSI (Problem Solving Index)
  - EI (Emotion Index)
  - LTMI (Learning Technical Metrics Index)
- Create Analysis Record
- View Analysis Results

**D. Analysis Publishing**
- Decide to Publish/Draft
- Mark Analysis as Published
- Make Visible to All Users
- Keep as Draft

**E. Advanced Analysis (Bloom's Taxonomy)**
- Technical Analysis Upload
- Upload Technical Dataset
- Validate Technical Data Structure
- Compute Bloom's Taxonomy Weighted Metrics
- Save Enriched Dataset
- Technical Dashboard Visualization
- Export Results & Charts

**F. Analysis Management**
- View All Created Analyses
- Edit Analysis Details
- Publish/Unpublish
- Delete Analysis

**G. System Configuration**
- View Configuration Settings
- Adjust System Parameters

### Admin Flowchart (Mermaid Code):

```mermaid
flowchart TD
    Start([Start]) --> Register[Register/Login to System]
    Register --> AdminDash[Access Admin Dashboard]
    AdminDash --> CheckAction{Select Action}
    
    CheckAction -->|Data Management| Upload[Upload Data File]
    Upload --> ValidateFile{File Valid?}
    ValidateFile -->|No| ErrorUpload[Show Error Message]
    ErrorUpload --> Upload
    ValidateFile -->|Yes| SaveFile[Save File to System]
    SaveFile --> DeactivatePrev[Deactivate Previous Files]
    DeactivatePrev --> DataMgr[Data Manager - View Files]
    
    DataMgr --> ManageFile{Manage Action}
    ManageFile -->|Activate| Activate[Set as Active Dataset]
    ManageFile -->|Archive| Archive[Archive Inactive Files]
    ManageFile -->|Download| Download[Download Dataset]
    Activate --> DataMgr
    Archive --> DataMgr
    Download --> DataMgr
    
    DataMgr --> BackToDash1[Return to Dashboard]
    BackToDash1 --> CheckAction
    
    CheckAction -->|Analysis| QuickAnalyze[Quick Analysis Creation]
    QuickAnalyze --> SelectFile[Select Active Data File]
    SelectFile --> ValidateData{Validate Data<br/>Against Schema}
    ValidateData -->|No| ShowError[Display Validation Errors]
    ShowError --> QuickAnalyze
    ValidateData -->|Yes| ComputeMetrics[Compute Paper-Compliant Metrics<br/>TI, NTI, CMI_P]
    ComputeMetrics --> GenerateStats[Generate Summary Statistics<br/>CUI, CDI, CCI, PSI, EI]
    GenerateStats --> CreateAnalysis[Create Analysis Record]
    CreateAnalysis --> ViewAnalysis[View Analysis Results]
    
    ViewAnalysis --> DecidePublish{Publish Analysis?}
    DecidePublish -->|Yes| Publish[Mark Analysis as Published]
    Publish --> MakeVisible[Make Visible to All Users]
    DecidePublish -->|No| KeepDraft[Keep as Draft]
    MakeVisible --> BackToDash2[Return to Dashboard]
    KeepDraft --> BackToDash2
    BackToDash2 --> CheckAction
    
    CheckAction -->|Advanced Analysis| TechAnalysis[Technical Analysis Upload]
    TechAnalysis --> UploadTechFile[Upload Technical Dataset]
    UploadTechFile --> ValidateTech{Validate Technical<br/>Data Structure}
    ValidateTech -->|No| ErrorTech[Show Validation Error]
    ErrorTech --> TechAnalysis
    ValidateTech -->|Yes| EnrichData[Compute Bloom's Taxonomy<br/>Weighted Metrics]
    EnrichData --> SaveEnriched[Save Enriched Dataset<br/>with Computed Indices]
    SaveEnriched --> TechDash[Technical Dashboard<br/>Visualization]
    TechDash --> ExportResults[Export Results & Charts]
    ExportResults --> BackToDash3[Return to Dashboard]
    BackToDash3 --> CheckAction
    
    CheckAction -->|Configuration| Config[View Configuration Settings]
    Config --> BackToDash4[Return to Dashboard]
    BackToDash4 --> CheckAction
    
    CheckAction -->|View Analyses| ViewAll[View All Created Analyses]
    ViewAll --> ManageAnalyses{Manage Analysis}
    ManageAnalyses -->|Edit| EditAnalysis[Modify Analysis Details]
    ManageAnalyses -->|Publish| PublishAnalysis[Publish to Users]
    ManageAnalyses -->|Unpublish| UnpublishAnalysis[Hide from Users]
    ManageAnalyses -->|Delete| DeleteAnalysis[Remove Analysis]
    EditAnalysis --> ViewAll
    PublishAnalysis --> ViewAll
    UnpublishAnalysis --> ViewAll
    DeleteAnalysis --> ViewAll
    ViewAll --> BackToDash5[Return to Dashboard]
    BackToDash5 --> CheckAction
    
    CheckAction -->|Logout| Logout[Logout from System]
    Logout --> End([End])
    
    style Start fill:#90EE90
    style End fill:#FFB6C6
    style AdminDash fill:#87CEEB
    style Upload fill:#FFD700
    style DataMgr fill:#FFD700
    style QuickAnalyze fill:#DDA0DD
    style TechAnalysis fill:#DDA0DD
    style ViewAnalysis fill:#DDA0DD
    style Publish fill:#98FB98
    style Config fill:#F0E68C
    style Logout fill:#FFB6C6
```

---

## 2. User Methodology Flowchart

The User flowchart illustrates how users access, view, and interact with published analyses and research data.

### User Workflow Components:

**A. Authentication**
- Register/Login to System
- Access User Dashboard

**B. Dashboard Navigation**
- Load Published Analyses from Database
- Display Research Statistics:
  - Total Participants
  - Research Areas
  - Available Studies

**C. View Analysis**
- Select Published Analysis
- Validate Access Permissions
- Load Analysis Metrics from Database
- Display Summary Statistics:
  - CUI, CDI, CCI
  - PSI, EI, LTMI
  - TI, NTI, CMI_P
- Visualize Data:
  - Distribution Charts
  - Mean & Standard Deviation
  - Expertise Levels
- Explore Detailed Data:
  - View Participant Details
  - Individual Metrics
  - Performance Distribution
- Download Report (PDF/Excel)

**D. User Profile**
- Access User Profile Page
- View Profile Information:
  - Username
  - Email
  - Registration Date
- View Analysis History:
  - Total Analyses Viewed
  - Last Viewed Analysis
  - Research Participation
- Profile Actions:
  - Edit Profile
  - View Research Preferences
  - Save Changes

**E. Browse Studies**
- List All Published Analyses
- Filter/Sort Options:
  - By Publication Date
  - By Title
  - By Participant Count
- Display Analyses List with Metadata
- Select Analysis for Viewing

**F. Exit**
- Logout from System

### User Flowchart (Mermaid Code):

```mermaid
flowchart TD
    Start([Start]) --> Register[Register/Login to System]
    Register --> UserDash[Access User Dashboard]
    
    UserDash --> LoadAnalyses[Load Published Analyses<br/>from Database]
    LoadAnalyses --> DisplayStats[Display Research Statistics<br/>Total Participants<br/>Research Areas<br/>Available Studies]
    
    DisplayStats --> CheckAction{Select Action}
    
    CheckAction -->|View Analysis| SelectAnalysis[Select Published Analysis]
    SelectAnalysis --> ValidateAccess{Analysis<br/>Published?}
    ValidateAccess -->|No| NotFound[Analysis Not Found<br/>or Not Published]
    NotFound --> UserDash
    
    ValidateAccess -->|Yes| LoadMetrics[Load Analysis Metrics<br/>from Database]
    LoadMetrics --> DisplayMetrics[Display Summary Statistics<br/>CUI, CDI, CCI<br/>PSI, EI, LTMI<br/>TI, NTI, CMI_P]
    
    DisplayMetrics --> ShowCharts[Visualize Data<br/>Distribution Charts<br/>Mean & Std Dev<br/>Expertise Levels]
    
    ShowCharts --> ExploreData{Explore Further?}
    ExploreData -->|View Details| Details[View Participant Details<br/>Individual Metrics<br/>Performance Distribution]
    ExploreData -->|Download Report| Export[Download Analysis Report<br/>as PDF/Excel]
    ExploreData -->|Back| UserDash
    
    Details --> MoreOptions{Continue?}
    MoreOptions -->|View More| ShowCharts
    MoreOptions -->|Back| UserDash
    
    Export --> BackAfterExport[Return to Dashboard]
    BackAfterExport --> UserDash
    
    CheckAction -->|View Profile| UserProfile[Access User Profile Page]
    UserProfile --> ProfileInfo[Display Profile Information<br/>Username<br/>Email<br/>Registration Date]
    
    ProfileInfo --> ViewHistory[View Analysis History<br/>Total Analyses Viewed<br/>Last Viewed Analysis<br/>Research Participation]
    
    ViewHistory --> ProfileAction{Profile Action}
    ProfileAction -->|Edit Profile| EditProfile[Modify User Details]
    ProfileAction -->|View Preferences| Prefs[View Research Preferences]
    ProfileAction -->|Back| UserDash
    
    EditProfile --> SaveChanges[Save Updated Profile]
    SaveChanges --> UserDash
    
    Prefs --> UserDash
    
    CheckAction -->|Browse Studies| BrowseAll[List All Published Analyses]
    BrowseAll --> FilterSort{Filter/Sort?}
    FilterSort -->|By Date| SortDate[Sort by Publication Date]
    FilterSort -->|By Title| SortTitle[Sort by Title]
    FilterSort -->|By Participants| SortParticip[Sort by Participant Count]
    FilterSort -->|None| NoSort[View All]
    
    SortDate --> DisplayList[Display Analyses List<br/>with Metadata]
    SortTitle --> DisplayList
    SortParticip --> DisplayList
    NoSort --> DisplayList
    
    DisplayList --> SelectFromList{Select Analysis}
    SelectFromList -->|Yes| SelectAnalysis
    SelectFromList -->|No| UserDash
    
    CheckAction -->|Logout| Logout[Logout from System]
    Logout --> End([End])
    
    style Start fill:#90EE90
    style End fill:#FFB6C6
    style UserDash fill:#87CEEB
    style SelectAnalysis fill:#DDA0DD
    style DisplayMetrics fill:#DDA0DD
    style ShowCharts fill:#DDA0DD
    style UserProfile fill:#F0E68C
    style ProfileInfo fill:#F0E68C
    style BrowseAll fill:#FFD700
    style DisplayList fill:#FFD700
    style Export fill:#98FB98
    style Logout fill:#FFB6C6
```

---

## How to Use These Flowcharts in Your Research Project

### Option 1: Embed in Research Paper (Markdown)
Copy the Mermaid code directly into your markdown or LaTeX document.

### Option 2: Export as Images
Use online Mermaid editors to export as PNG/SVG:
- Visit: https://mermaid.live
- Paste the flowchart code
- Download as image

### Option 3: Use in Presentation
Include the flowcharts in PowerPoint, Google Slides, or other presentations by exporting to image format.

### Option 4: Reference in Documentation
Include the code in technical documentation, GitHub wikis, or online documentation platforms that support Mermaid.

---

## Color Legend

- **Green** (`#90EE90`): Start/End Points
- **Light Blue** (`#87CEEB`): Main Dashboard/Entry Points
- **Gold** (`#FFD700`): Data Management Functions
- **Plum** (`#DDA0DD`): Analysis Functions
- **Light Green** (`#98FB98`): Critical Actions (Publish/Export)
- **Khaki** (`#F0E68C`): User Profile & Configuration
- **Pink** (`#FFB6C6`): Logout/End Actions

---

## Metrics Explained

### Cognitive Indices
- **CUI** - Cognitive Understanding Index
- **CDI** - Cognitive Debugging Index
- **CCI** - Cognitive Completion Index
- **PSI** - Problem Solving Index
- **EI** - Emotion Index
- **LTMI** - Learning Technical Metrics Index

### Paper-Compliant Metrics
- **TI** - Technical Index
- **NTI** - Non-Technical Index
- **CMI_P** - Comprehensive Metrics Index (Paper)

### Bloom's Taxonomy Indices
- **T1** - Knowledge/Understanding (Level 1)
- **T2** - Application/Analysis (Level 2)
- **T3** - Synthesis/Evaluation (Level 3)
- **CL1** - Cognitive Load Index 1
- **CL1_Div3_Scaled** - Scaled Cognitive Load Metric

---

## Document Information

- **System**: Cognitive & Emotional Performance Research Dashboard
- **Created**: February 2026
- **Purpose**: Research Project Documentation
- **Format**: Mermaid Flowcharts (Markdown)
- **Version**: 1.0

---

## Notes for Research Inclusion

1. These flowcharts represent the actual implementation methodology of the system
2. Different user roles (Admin vs Regular User) have distinct workflows
3. The system implements paper-compliant metrics for cognitive research
4. Data validation and error handling are integral parts of the workflow
5. The system supports multiple analysis types with different computational approaches

---

*This document can be included in your research project, thesis, dissertation, or technical documentation. Feel free to customize the flowcharts to match your specific requirements.*
