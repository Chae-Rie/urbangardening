
// UrbanGardeningDlg.h : header file
//

#pragma once


// CUrbanGardeningDlg dialog
class CUrbanGardeningDlg : public CDialogEx
{
// Construction
public:
	CUrbanGardeningDlg(CWnd* pParent = nullptr);	// standard constructor

// Dialog Data
#ifdef AFX_DESIGN_TIME
	enum { IDD = IDD_URBANGARDENING_DIALOG };
#endif

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV support


// Implementation
protected:
	HICON m_hIcon;

	// Generated message map functions
	virtual BOOL OnInitDialog();
	afx_msg void OnSysCommand(UINT nID, LPARAM lParam);
	afx_msg void OnPaint();
	afx_msg HCURSOR OnQueryDragIcon();
	
	// Eigene Methoden
	virtual BOOL DestroyWindow();

	DECLARE_MESSAGE_MAP()

	void ChangeAccess(BOOL CanConnect);
};
